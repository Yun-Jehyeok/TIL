# 실버 5
data = str(input())

# 크로아티아 알파벳 다 숫자로 바꾸기
data = data.replace('c=', '1')
data = data.replace('c-', '2')
data = data.replace('dz=', '3')
data = data.replace('d-', '4')
data = data.replace('lj', '5')
data = data.replace('nj', '6')
data = data.replace('s=', '7')
data = data.replace('z=', '8')

# 숫자 카운트
numsCnt = [0] * 8
# 알파벳 카운트
alphaCnt = [0] * 26

# 문자열을 리스트로 바꿔주고
data = list(data)

for val in data:
    # 알파벳이면
    if val.isalpha():
        cur = ord(val) - 97
        alphaCnt[cur] += 1
    else: # 숫자면
        numsCnt[int(val) - 1] += 1

print(sum(numsCnt) + sum(alphaCnt))