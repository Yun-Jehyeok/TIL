import sys
from collections import deque

N, M, H = map(int, sys.stdin.readline().strip().split())

graph = []

for i in range(H):
    data = []

    for j in range(M):
        data.append(list(map(int, sys.stdin.readline().strip().split())))

    graph.append(data)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque([])

    for i in range(H):
        for j in range(M):
            for k in range(N):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= H or ny >= M or nz >= N:
                continue

            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx, ny, nz))

bfs()

flag = False

for i in range(H):
    for j in range(M):
        for k in range(N):
            if graph[i][j][k] == 0:
                flag = True

if flag:
    print(-1)
else:
    max = -1

    for i in range(H):
        for j in range(M):
            for k in range(N):
                if graph[i][j][k] != 0:
                    if max < graph[i][j][k]:
                        max = graph[i][j][k]

    print(max - 1)