# 내가 생각한 답
N = int(input())
adv = list(map(int, input().split()))

adv.sort(reverse=True) # O(NlogN)

cnt = 0

while True:
    if len(adv) == 0 or len(adv) < adv[0]:
        break
    else:
        adv = adv[adv[0]:]
        cnt += 1

print(cnt)


# 정답
N = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in data:
	count += 1 # 현재 그룹에 해당 모험가 포함시키기

    # 현재 그룹에 포함된 모험가 수가 현재의 공포도 이상이면, 그룹 결성
    # [1, 2, 2, 2, 3] 이면
    # [1], [2, 2] 까지 되고 [2, 3]은 되지 않고 반복문이 멈춰진다.
	if count >= i:
		result += 1
		count = 0

print(result)