# 실버 5
N = int(input())

# 결과값
result = 0

for i in range(N):
    # 알파벳 리스트로 입력
    alphabets = list(str(input()))

    # 그룹이 아닌 알파벳 카운트
    alphabetCnt = [0] * 26
    # 이전 알파벳(-1은 없는 수)
    prev = -1

    # 입력 받은 단어의 모든 알파벳에 대해
    for alphabet in alphabets:
        # 알파벳을 0~25 사이의 숫자로 반환
        cur = ord(alphabet) - 97

        # 이전 문자와 현재 문자가 다르면
        if prev != cur:
            # 해당 알파벳 카운트
            alphabetCnt[cur] += 1
            # 이전 문자를 현재 문자로
            prev = cur
    
    # 그룹 단어 체크 변수
    isSuc = True

    # 알파벳 카운트에 대해
    for cnt in alphabetCnt:
        # 카운트가 2번 이상인 경우가 하나라도 있다면
        # 즉, aba와 같은 경우 [2, 1, 0, 0, ...]이 되기 때문에 실패
        if cnt >= 2:
            isSuc = False
    
    # 성공시 결과값 + 1
    if isSuc:
        result += 1


print(result)