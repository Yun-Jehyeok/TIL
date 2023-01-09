import sys

sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())

    graph = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[y][x] = 1

    def dfs(x, y):
        if x <= -1 or y <= -1 or x >= N or y >= M:
            return False

        if graph[x][y] == 1:
            graph[x][y] = 0

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

            return True

        return False

    result = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if dfs(i, j):
                    result += 1

    print(result)