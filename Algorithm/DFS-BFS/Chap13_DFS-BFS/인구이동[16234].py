import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().strip().split())
graph = []
visited = [[False] * N for _ in range(N)]

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    sum = graph[x][y]
    cnt = 1
    isDayPass = False

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
                continue

            if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                sum += graph[nx][ny]
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx, ny))

    if cnt >= 2:
        isDayPass = True

        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    graph[i][j] = int(sum / cnt)

    return graph, isDayPass

day = 0

while True:
    dayPass = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                graph, isDayPass = bfs(i, j)
                visited = [[False] * N for _ in range(N)]
                
                if isDayPass:
                    dayPass = True
                    break

    if dayPass:
        day += 1
        visited = [[False] * N for _ in range(N)]
    else:
        break

print(day)