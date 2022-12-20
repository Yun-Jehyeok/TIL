# 2206
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

graph = []
# 방문처리에 벽을 부쉈는지 안부쉈는지 추가
# 0이면 부수지 않음
# 1이면 부숨
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] 
visited[0][0][0] = 1 # 거리는 1부터 시작

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque([(x, y, z)])

    while queue:
        x, y, z = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 벽인데 아직 한번도 안부쉈으면
            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))

            # 길이고 방문하지 않았으면
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

    return -1

print(bfs(0, 0, 0))