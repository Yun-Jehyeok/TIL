import copy


def solution(key, lock):
    M, N = len(key), len(lock)
    
    answer = False

    # 자물쇠 빈 칸의 위치 좌표
    lock_locs = []

    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                lock_locs.append([i, j])

    # 상하좌우로 0~M만큼 움직여서 모든 데이터를 move_keys에 저장 
    # move_keys는 3차원 배열이 됨
    move_keys = []

    move_key = []
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                move_key.append([i, j])

    # 처음 움직이지 않았을 때의 좌표
    move_keys.append(move_key)

    # 네 방향으로 이동하면서 모든 데이터 저장
    for i in range(4):
        # 첫 위치좌표 복사
        tmp_keys = copy.deepcopy(move_key)

        # M번만큼 이동
        for _ in range(M):
            # 첫 위치 좌표의 모든 키들에 대해서
            for tmp_key in tmp_keys:
                if i == 0: # 상
                    tmp_key[0] -= 1
                elif i == 1: # 하
                    tmp_key[0] += 1
                elif i == 2: # 좌
                    tmp_key[1] -= 1
                else: # 우
                    tmp_key[1] += 1

            move_keys.append(tmp_keys)

    # 회전 없이 이동만 했던 모든 키들에 대해서
    for move_key in move_keys:
        tmp_keys = copy.deepcopy(move_key) # 복사 후
        rotate_keys = [] # 4번 회전한 데이터들 # 3차원 배열
        rotate_keys.append(tmp_keys) # 처음 회전 안 했을 경우 추가

        # 3번 회전
        for i in range(3):
            rotate_key = []

            for tmp_key in tmp_keys:
                # 회전 후의 행 = 회전 전의 열, 회전 후의 열 = key 전체 배열의 마지막 인덱스 - 회전 전의 행
                x, y = tmp_key[1], M - 1 - tmp_key[0]
                rotate_key.append([x, y])

            rotate_keys.append(rotate_key)
            tmp_keys = copy.deepcopy(rotate_key)

        # 모든 회전한 데이터들에 대해
        for rotate_key in rotate_keys:
            flag = True # 자물쇠와 열쇠가 맞는지에 대한 플래그

            # 자물쇠의 모든 좌표에 대해
            for lock_loc in lock_locs:
                # 좌물쇠의 각 좌표가 회전한 데이터에 없으면 -> 맞지 않는 열쇠인 경우
                if lock_loc not in rotate_key:
                    flag = False
                    break # 종료
            
            # 자물쇠와 열쇠가 맞을 경우
            if flag:
                more_flag = True

                # 자물쇠랑 돌기랑 겹치는 것 확인
                for key in rotate_key:
                    if key[0] >= 0 and key[1] >= 0 and key[0] < M and key[1] < M and key not in lock_locs:
                        more_flag = False
                        
                # 자물쇠 돌기랑 열쇠가 겹치는 경우가 없을 경우
                if more_flag:
                    answer = True
                    break

        # answer가 True면 종료
        # 종료 안하면 다음 데이터에 대한 계산을 다시 하기 때문에 False로 바뀜
        if answer:
            break

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 정답 코드

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False

    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠 크기를 기존의 3배로
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 값 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전

        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock):
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False