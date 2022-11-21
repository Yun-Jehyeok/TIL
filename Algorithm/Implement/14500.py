# 14500
# ㅋㅋ... 나처럼 일반 브루트 포스 + 구현으로만 풀 수도 있고
# DFS를 사용해서 풀 수도 있다고 한다.
# 뭐 어때 20분도 안걸려서 맞았으면 됐지
# 참고로 삼성 문제라고 한다.
# 그래도 DFS로 섹시하게 풀고싶다.
import sys

N, M = map(int, sys.stdin.readline().strip().split())

commands = [
    [(0, 0), (0, 1), (0, 2), (0, 3)], # 일자
    [(0, 0), (1, 0), (2, 0), (3, 0)], # 일자
    [(0, 0), (0, 1), (1, 0), (1, 1)], # 정사각형
    [(0, 0), (1, 0), (2, 0), (2, 1)], # ㄴ자
    [(0, 0), (1, 0), (2, 0), (2, -1)], # ㄴ자
    [(0, 0), (0, 1), (1, 0), (2, 0)], # ㄴ자
    [(0, 0), (0, 1), (1, 1), (2, 1)], # ㄴ자
    [(0, 0), (1, 0), (1, 1), (1, 2)], # ㄴ자
    [(0, 0), (1, 0), (0, 1), (0, 2)], # ㄴ자
    [(0, 0), (1, 0), (1, -1), (1, -2)], # ㄴ자
    [(0, 0), (0, 1), (0, 2), (1, 2)], # ㄴ자
    [(0, 0), (1, 0), (1, 1), (2, 1)], # 지그재그
    [(0, 0), (0, 1), (-1, 1), (-1, 2)], # 지그재그
    [(0, 0), (1, 0), (1, -1), (2, -1)], # 지그재그
    [(0, 0), (0, 1), (1, 1), (1, 2)], # 지그재그
    [(0, 0), (0, 1), (0, 2), (1, 1)], # 볼록
    [(0, 0), (0, 1), (-1, 1), (1, 1)], # 볼록
    [(0, 0), (0, 1), (0, 2), (-1, 1)], # 볼록
    [(0, 0), (1, 0), (2, 0), (1, 1)], # 볼록
]

datas = []

for i in range(N):
    data = list(map(int, sys.stdin.readline().strip().split()))
    datas.append(data)

find_max = []

for i in range(N):
    for j in range(M):
        for command in commands:
            nx1 = i + command[0][0]
            ny1 = j + command[0][1]
            nx2 = i + command[1][0]
            ny2 = j + command[1][1]
            nx3 = i + command[2][0]
            ny3 = j + command[2][1]
            nx4 = i + command[3][0]
            ny4 = j + command[3][1]

            if nx1 >= 0 and nx1 < N and nx2 >= 0 and nx2 < N and nx3 >= 0 and nx3 < N and nx4 >= 0 and nx4 < N:
                if ny1 >= 0 and ny1 < M and ny2 >= 0 and ny2 < M and ny3 >= 0 and ny3 < M and ny4 >= 0 and ny4 < M:
                    sum = datas[nx1][ny1] + datas[nx2][ny2] + datas[nx3][ny3] + datas[nx4][ny4]
                    find_max.append(sum)

print(max(find_max))