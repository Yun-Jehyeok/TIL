import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

graph = []
visited = [[False] * N for _ in range(N)]

for i in range(N):
    data = list(map(int, sys.stdin.readline().strip().split()))
    graph.append(data)

    for j in range(N):
        if data[j] != 0:
            visited[i][j] = True

S, X, Y = map(int, sys.stdin.readline().strip().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0

def bfs():
    datas = [(0, 0)]
    queue = deque(datas)

    while queue:
        data = queue.popleft()
        x = data[0]
        y = data[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if (graph[nx][ny] == 0 or graph[nx][ny] > graph[x][y]) and (not visited[nx][ny]):
                graph[nx][ny] = graph[x][y]
                queue.append((nx, ny))

while time < S:
    bfs()

    time += 1


print(graph[X - 1][Y - 1])