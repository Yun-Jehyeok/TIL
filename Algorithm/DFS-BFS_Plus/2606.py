import sys
from collections import deque

computers = int(sys.stdin.readline())
N = int(sys.stdin.readline())

graph = [ [False] * (computers + 1) for _ in range(computers + 1) ]

for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x][y] = True
    graph[y][x] = True

def bfs(start):
    discovered = [start]
    queue = deque([start])

    cnt = 0

    while queue:
        v = queue.popleft()

        for i in range(computers + 1):
            if graph[v][i] and (i not in discovered):
                discovered.append(i)
                queue.append(i)
                cnt += 1

    print(cnt)

bfs(1)