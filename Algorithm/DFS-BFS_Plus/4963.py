import sys
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(graph, visited, x, y, group):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = group
                visited[nx][ny] = True

    return visited

while True:
    w, h = map(int, sys.stdin.readline().strip().split())

    if w == 0 and h == 0:
        break

    graph = []
    visited = [ [False] * w for _ in range(h) ]
    group = 0

    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                group += 1
                visited = bfs(graph, visited, i, j, group)

    print(group)