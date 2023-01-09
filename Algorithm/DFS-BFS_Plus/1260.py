import sys
from collections import deque

# N = 정점 수, M = 간선 수
N, M, V = map(int, sys.stdin.readline().strip().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x][y] = graph[y][x] = 1

def bfs(start):
    discovered = [start]
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(N + 1):
            if graph[v][i] == 1 and (i not in discovered):
                discovered.append(i)
                queue.append(i)

def dfs(start, stack=[]):
    stack.append(start)
    print(start, end=' ')

    for i in range(N + 1):
        if graph[start][i] == 1 and (i not in stack):
            dfs(i, stack)

dfs(V)
print()
bfs(V)