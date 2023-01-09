import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

graph = []

for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([])

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()

flag = False

for i in range(N):
    for j in range(M):
        if graph[j][i] == 0:
            flag = True

if flag:
    print(-1)
else:
    print(max(map(max, graph)) - 1)