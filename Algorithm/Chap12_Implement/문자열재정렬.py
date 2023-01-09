# 내 정답
data = list(input())

strs = [x for x in data if x >= 'A' and x <= 'Z']
nums = [int(x) for x in data if x >= '0' and x <= '9']

strs.sort()

print(''.join(strs) + str(sum(nums)))

# 정답 코드
data = list(input())

strs = [x for x in data if x.isalpha()]
nums = [int(x) for x in data if not x.isalpha()]

strs.sort()

print(''.join(strs) + str(sum(nums)))