# 첫 번째 코드(에러)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

maxVal = data[n - 1]
secondMaxVal = data[n - 2]

result = 0

result += maxVal * (m - (m % k)) + secondMaxVal * (m % k)

print(result)


# 위 코드 수정(에러)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

maxVal = data[n - 1]
secondMaxVal = data[n - 2]

maxCnt = m // k * k # 횟수 나누기 반복 가능의 몫 * 반복 가능
maxCnt += (m % k) % (m // k) # 나머지 나누기 수열이 반복된 횟수의 몫

result = 0

result += maxVal * maxCnt + secondMaxVal * (m - maxCnt)

print(result)


# 정답 코드
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

maxVal = data[n - 1]
secondMaxVal = data[n - 2]

maxCnt = m // k * k # 횟수 나누기 반복 가능의 몫 * 반복 가능
maxCnt += (m % k) % (m // k) # 나머지 나누기 수열이 반복된 횟수의 몫

result = 0

result += maxVal * maxCnt + secondMaxVal * (m - maxCnt)

print(result)