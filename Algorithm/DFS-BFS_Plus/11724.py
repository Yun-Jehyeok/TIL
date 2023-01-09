import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

visited = [False] * (N + 1)
graph = [ [] for _ in range(N + 1) ]

for i in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())

    # 무방향 그래프니까
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):    
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)