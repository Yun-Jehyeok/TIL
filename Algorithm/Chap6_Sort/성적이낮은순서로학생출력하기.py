import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    x, y = sys.stdin.readline().strip().split()
    arr.append((x, int(y)))

arr = sorted(arr, key=lambda x: x[1])

for data in arr:
    print(data[0], end=' ')