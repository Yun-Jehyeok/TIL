# 백준 1026
from copy import deepcopy as dc
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

bTmp = dc(B)
aTmp = A
aResult = [0] * N

for i in range(N):
    bMaxIdx = bTmp.index(max(bTmp))
    aMinIdx = aTmp.index(min(aTmp))
    aMin = min(aTmp)

    aResult[bMaxIdx] = aMin

    bTmp[bMaxIdx] = -1
    aTmp[aMinIdx] = 101

result = 0

for i in range(N):
    result += aResult[i] * B[i]

print(result)