# 내 코드
# 하다가 실패 - 삭제 쪽 메서드 짜려다 보니... 이 방법으로는 안될듯
# 기둥 설치
def set_column(n, arr, x, y):
    if y + 1 <= n: # 기둥 설치가 좌표 평면 안에서 실행될경우
        if y == 0 or arr[x][y] == 2 or arr[x][y] == 1: # 바닥이거나 해당 좌표에 보가 있거나 기둥 위거나
            arr[x][y] = 1
            arr[x][y + 1] = 1

    return arr

# 기둥 삭제
def del_column(arr, x, y):
    return arr

# 보 설치
def set_girder(n, arr, x, y):
    if x + 1 <= n:
        if arr[x][y] == 1 or (arr[x][y] == 2 and arr[x + 1][y] == 2):
            arr[x][y] = 2
            arr[x + 1][y] = 2

    return arr

# 보 삭제
def del_girder(arr, x, y):
    return arr

def solution(n, build_frame):
    answer = []
    # 맵 만들기
    # 교차점에 대한 정보를 가져야 되기 때문에 크기가 1만큼 더 커야됨
    map = [[0] * (n + 1) for _ in range(n + 1)] 

    # 각각의 build_frame에 대해
    for step in build_frame:
        x, y, a, b = step[0], step[1], step[2], step[3]
        
        if a == 0: # 기둥일 경우
            if b == 0: # 삭제의 경우
                del_column(map, x, y)
            else: # 추가의 경우
                set_column(n + 1, map, x, y)
        else: # 보의 경우
            if b == 0: # 삭제의 경우
                del_girder(map, x, y)
            else: # 추가의 경우
                set_girder(n + 1, map, x, y)

    # 맵의 모든 정보에 대해
    for i in range(n + 1):
        for j in range(n + 1):
            if map[i][j] != 0: # 값이 0이 아니면(기둥 또는 보가 설치되어 있으면)
                result = [i, j, map[i][j] - 1] # [x, y, 건축물]
                answer.append(result) # 정답에 추가

    # x, y 순서로 오름차순 정렬
    answer = sorted(answer, key = lambda x: (x[0], x[1]))

    return answer


# 정답 코드

# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥일 경우
            # 바닥 위 혹은 보의 한쪽 끝부분 위 혹은 다른 기둥 위라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue

            # 아니라면
            return False
        elif stuff == 1: # 보인 경우
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue

            # 아니라면
            return False
    
    return True

def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame

        if operate == 0: # 삭제의 경우
            answer.remove([x, y, stuff])
            
            if not possible(answer):
                answer.append([x, y, stuff])
        
        if operate == 1: # 설치의 경우
            answer.append([x, y, stuff])

            if not possible(answer):
                answer.remove([x, y, stuff])
    
    return sorted(answer)