# 아이디어
# 각 무게들을 배열에 담아 오름차순 정렬
# 각 무게를 가질 수 있는 최대값을 max_weights 배열에 담아 그 중 최대값 출력
N = int(input())

weights = [] # 각 로프가 들 수 있는 무게
max_weights = [] # 각 로프를 사용해 들 수 있는 최대 무게

for i in range(N):
    weight = int(input())
    weights.append(weight)
    
weights.sort() # 오름차순 정렬

for i in range(N):
    max_weights.append(weights[i] * (N - i)) # 각 무게 * (로프 개수 - 현재 로프 인덱스)
    
print(max(max_weights))