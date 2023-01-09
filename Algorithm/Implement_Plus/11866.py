# 실버 5
N, K = map(int, input().split())
datas = [x for x in range(1, N + 1)]

currentIdx = -1 # datas에서 빠질 데이터의 인덱스
horse = 0 # K번째 사람 카운트
result = [] # 결과 저장

# 인덱스 이동
def move(idx, datasLen):
    idx += 1

    if idx == datasLen:
        idx = 0

    return idx

while True:
    # 데이터가 하나 남았으면
    if len(datas) == 1:
        result.append(datas[0])
        break

    horse += 1 # 카운트 다운
    currentIdx = move(currentIdx, len(datas)) # 인덱스 이동

    if horse == K: # K번째면
        data = datas.pop(currentIdx) # 데이터 빼와서
        result.append(data) # 결과에 저장
        horse = 0 # 카운트는 다시 0으로

        # 중간 사람이 하나 빠졌기에 -1
        # 예를 들어 (7, 3) 순열에서 처음으로 3번 사람이 빠졌으면 다음 검사할 사람은 4
        # 하지만 4의 인덱스가 2이므로 하나 빼줘야 됨
        currentIdx -= 1

result = list(map(str, result))
result = ', '.join(result)
print('<' + result + '>')