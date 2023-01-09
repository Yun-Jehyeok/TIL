# 내 정답
S = str(input())

# 예시 55-50+09
operators = [] # S의 연산자들을 넣을 배열

for data in S:
    if data == '-' or data == '+':
        operators.append(data) # 연산자 저장 -> ['-', '+']

S = S.replace('+', '-') # split 함수 사용을 위해 +를 모두 -로 변경 -> '55-50-09'

# 각 숫자를 int 타입으로 배열 저장 -> 09와 같은 수를 9로 바꾸기 위해 -> [55, 50, 9]
nums = list(map(int, S.split('-'))) 

# 다시 하나의 문자열로 변환
S = str(nums[0]) # 55
for i in range(1, len(nums)):
    S += operators[i - 1] + str(nums[i]) # 55-50+9
    
list_s = list(S) # ['5', '5', '-', '5', '0', '+', '9']

is_bracket_open = False # 괄호가 열려있는지 # default는 안열려있음

i = 0

while i < len(list_s): # ['5', '5', '-', '5', '0', '+', '9']에 대해
    if list_s[i] == '-': # 데이터가 '-'이면
        list_s.insert(i+1, '(') # - 다음에 열림 괄호 삽입

        if not is_bracket_open: # 만약 이전까지 한 번도 열린 적 없으면
            i += 1 # 열림 괄호 하나만 썼으므로 1만큼 i 추가
        else: # 한 번이라도 열린 적이 있다면 - 가 나올 때마다 )-( 가 되어야 한다.
            list_s.insert(i, ')') # - 앞에 ) 삽입
            i += 2 # (, ) 총 2개를 썼으니 i += 2

        is_bracket_open = True # 어찌됐든 - 가 나왔다면 무조건 열림 상태가 됨
    
    i += 1 # 인덱스 진행

if is_bracket_open: # 반복 끝났는데 괄호가 열려있으면
    list_s.append(')') # 마지막에 닫힘 괄호 추가

S =  ''.join(s for s in list_s) # 배열을 문자열로 만들어주기

print(eval(S)) # 문자열로 된 계산식 계산 -> 쓰지 말라고는 하는데... 안쓰고... 할 수는 있는데 귀찮은데..?

# 올바른 정답
# - 를 기준으로 나눠 아이템들의 덧셈 연산을 해주고
# 각 계산된 값을 순서대로 빼주면 끝..
# 여기까지 생각이 전혀 못미쳤다.
import sys
eqs = sys.stdin.readline().split("-")
nums = []
for eq in eqs:
    nums.append(sum(map(int, eq.split("+"))))

print(nums[0] - sum(nums[1:]))