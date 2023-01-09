N = int(input())
data = []

for i in range(N):
    val = int(input())
    
    # 0이 아닌 경우
    if val != 0:
        # 추가
        data.append(val)
    else: # 0인 경우
        # 지우기
        data.pop()

print(sum(data))