# 내가 생각한 코드
n, m = map(int, input().split())

result = []

for i in range(n):
	data = list(map(int, input().split()))
	result.append(min(data))

print(max(result))


# 정답 코드
n, m = map(int, input().split())

result = 0

for i in range(n):
	data = list(map(int, input().split()))
	min_value = min(data)
	result = max(result, min_value)

print(result)