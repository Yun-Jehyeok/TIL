# 실버 3
from collections import deque

T = int(input())

# 찾고자 하는 인덱스 이동
def move_m(queue, M):
    M -= 1

    if M == -1:
        M = len(queue) - 1

    return M

for _ in range(T):
    N, M = map(int, input().split())

    datas = list(map(int, input().split()))
    queue = deque(datas)

    # 하나씩 인쇄될 때(첫 번째 값이 최대인 경우) + 1
    cnt = 0

    while True:
        # 첫 번째 값이 최대가 아닐 경우
        if queue[0] != max(queue):
            data = queue.popleft() # 빼서
            queue.append(data) # 맨 뒤로
            M = move_m(queue, M)
        # 첫 번째 값이 최대인 경우
        else:
            # 카운트 증가
            cnt += 1

            # 찾고자 했던 값이 인쇄될 경우
            if M == 0:
                print(cnt)
                break
            else: # 찾고자 했던 값이 아닐 경우
                queue.popleft() # 빼기만
                M = move_m(queue, M)