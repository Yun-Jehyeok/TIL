import sys

N = list(str(sys.stdin.readline().strip()))

midIdx = len(N) // 2

leftSum = 0
rightSum = 0

for i in range(midIdx):
    leftSum += int(N[i])
for i in range(midIdx, len(N)):
    rightSum += int(N[i])
    
if leftSum == rightSum:
    print("LUCKY")
else:
    print("READY")