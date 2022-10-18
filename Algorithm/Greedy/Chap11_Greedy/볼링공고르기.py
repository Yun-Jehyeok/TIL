# 내가 생각한 코드
N, M = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        if data[i] != data[j]:
            cnt += 1
            
print(cnt)

# 답
N, M = map(int, input().split())
data = list(map(int, input().split()))

arr = [0] * 11

for x in data:
	arr[x] += 1

result = 0

for i in range(1, m + 1):
	n -= arr[i]
	result += arr[i] * n