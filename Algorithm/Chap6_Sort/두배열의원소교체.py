import sys

N, K = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

print(sum(A))