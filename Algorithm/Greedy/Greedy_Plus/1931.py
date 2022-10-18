##################################################
# 첫 번째 아이디어
# 1. 맨 처음 끝나는 시간이 제일 짧은 회의실을 잡는다.
# 2. 이후 이전 회의의 끝나는 시간 이후의 회의실 중 끝나는 시간이 제일 짧은 회의실을 잡는다.
# 틀렸습니다.
N = int(input())

info = []

for i in range(N):
    start, end = map(int, input().split())
    info.append((start, end))
    
info = sorted(info, key=lambda x: x[1]) # 끝나는 시간 기준으로 오름차순 정렬

current_meeting = info[0] # 0번 인덱스의 끝나는 시간이 제일 짧기 때문에 default는 0번 인덱스 값
cnt = 1 # 첫 회의는 들어갔기에 1

while True:
    new_info = [x for x in info if x[0] >= current_meeting[1]] # 남은 미팅 중 시작 시간이 현재 미팅의 끝나는 시간 이상인 미팅들만
    
    if len(new_info) == 0: # 그런 미팅이 없을 경우 종료
        break
    
    # 미팅이 있을 남아있을 경우
    # 남은 미팅 중 첫 번째 미팅을 현재 미팅으로 전환
    # 어차피 끝나는 시간 기준으로 오름차순 정렬 되어있기 때문에 괜찮음
    current_meeting = new_info[0] 
    cnt += 1
    
print(cnt)

##################################################
# 두 번째 아이디어
# 위와 아이디어는 같으나 정렬 수정
# lambda x: (x[1], x[0])과 같이 작성하면 x[1] 기준으로 정렬하고, x[1]의 값이 같은 경우 x[0]을 기준으로 정렬
# 시간 초과
N = int(input())

info = []

for i in range(N):
    start, end = map(int, input().split())
    info.append((start, end))
    
info = sorted(info, key=lambda x: (x[1], x[0]))

current_meeting = info[0]
cnt = 1

while True:
    new_info = [x for x in info if x[0] >= current_meeting[1]]
    
    if len(new_info) == 0:
        break
    
    current_meeting = new_info[0] 
    cnt += 1
    
print(cnt)

##################################################
# 세 번째 아이디어
# info에서 current_meeting 값을 삭제 시켜줘야되는 걸 간과했다.
# 만약 그게 아니라면 (1, 1)이라는 값이 있을 경우 여기서 계속 돌게 된다.
# 시간 초과 > 이제 뭐가 문제인지도 모르겠다.
N = int(input())

info = []

for i in range(N):
    start, end = map(int, input().split())
    info.append((start, end))
    
info = sorted(info, key=lambda x: (x[1], x[0]))

current_meeting = info[0]
cnt = 1
info.pop(0)

while True:
    info = [x for x in info if x[0] >= current_meeting[1]]
    
    if len(info) <= 0:
        break
    
    current_meeting = info[0]
    cnt += 1
    info.pop(0)

print(cnt)

##################################################
# 정답
# 뭐가 다른지도 모르겠다. 아이디어도 동일하고
# 근데 이게 훨씬 직관적이고 쉬워 보이기는 한다.
n = int(input())
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])

room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

cnt = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)