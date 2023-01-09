# 실버 5
datas = list(str(input()))
numCnt = [0] * 10

# 모든 데이터에 대해
for data in datas:
    # 9면 6이라 취급하고 넣기
    if int(data) == 9:
        numCnt[6] += 1
    else:
        numCnt[int(data)] += 1

# 한 세트에 6, 9 이렇게 있으므로 만약 6이 4개면 2세트, 5개면 3세트 필요
if numCnt[6] % 2 == 0:
    numCnt[6] = numCnt[6] // 2
else:
    numCnt[6] = numCnt[6] // 2 + 1

print(max(numCnt))