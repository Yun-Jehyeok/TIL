# 배열에서 i~j 인덱스 까지의 합을 구하는 방법
# 예를 들어 배열이 [5, 4, 3, 2, 1] 이고 0~2 까지의 합을 구하려면
# 보통 sum(datas[0:3]) 이렇게 할텐데
# 이 방법보단 prefix_sum 이라는 배열에 0~자기 자신까지의 합을 미리 구해서 넣어놓는게 
# 시간복잡도 상으로 더 좋다
# 백준 11659 번이 예시이다.

# 백준 11659 내 정답
# 시간복잡도가 O(MN) 이고 M = 10만, N = 10만으로 큰일난다.

import sys

N, M = map(int, sys.stdin.readline().strip().split())

datas = list(map(int, sys.stdin.readline().strip().split()))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(sum(datas[i - 1:j]))

# 누적합을 이용한 정답
# 시간복잡도가 O(N) 밖에 되지 않는다.
import sys

N, M = map(int, sys.stdin.readline().strip().split())

datas = list(map(int, sys.stdin.readline().strip().split()))

prefix_sum = [0] * N
prefix_sum[0] = datas[0]

for i in range(1, N):
    prefix_sum[i] = prefix_sum[i - 1] + datas[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())

    if i == 1:
        print(prefix_sum[j - 1])
    else:
        print(prefix_sum[j - 1] - prefix_sum[i - 2])
