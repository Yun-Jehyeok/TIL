n, m = map(int, input().split())
x, y, dir = map(int, input().split())

maps = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    data = list(map(int, input().split()))
    maps.append(data)
    
cnt = 1
turn_cnt = 0

while True:
    dir -= 1 # 회전
    turn_cnt += 1 # 회전 횟수 증가
    
    if dir < 0: # 0에서 회전하면 3으로
        dir = 3
        
		# 앞으로 전진
    nx = x + dx[dir]
    ny = y + dy[dir]
    
		# 이동한 좌표가 전체 직사각형 위에 있고
    if nx >= 0 and ny >= 0 and nx < n - 1 and ny < n - 1:
				# 이동한 곳이 육지면
        if maps[nx][ny] == 0:
						# 방문하고
            maps[nx][ny] = 1
						# 좌표도 바꾸고
            x = nx
            y = ny
						# 방문한 땅 횟수 증가
            cnt += 1
						# 회전 횟수 초기화
            turn_cnt = 0

		# 전 방향 다 돌았는데 갈 곳이 없으면 종료
    if turn_cnt == 3:
        break
    
print(cnt)