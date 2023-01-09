import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [-1, -2, -1, -2, 1, 2, 1, 2]
dy = [-2, -1, 2, 1, -2, -1, 2, 1]

def bfs(graph, L, x, y, des_x, des_y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        if x == des_x and y == des_y:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= L or ny >= L:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[des_x][des_y]

for _ in range(T):
    L = int(sys.stdin.readline())
    graph = [[0] * L for _ in range(L)]

    x, y = map(int, sys.stdin.readline().strip().split())
    des_x, des_y = map(int, sys.stdin.readline().strip().split())

    print(bfs(graph, L, x, y, des_x, des_y))