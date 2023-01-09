import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().strip().split())

graph = [ [] for _ in range(N + 1) ]
visited = [False] * (N + 1)
distance = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y)

def bfs(x):
    queue = deque([x])
    visited[x] = True
    distance[x] = 0

    answer = []

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1

                if distance[i] == K:
                    answer.append(i)

    return answer

answer = bfs(X)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    
    for data in answer:
        print(data)