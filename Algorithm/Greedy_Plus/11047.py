N, K = map(int, input().split())

data = []

for i in range(N):
    coin_val = int(input())
    
    if coin_val <= K: # K 이하인 값들만 배열에 저장
        data.append(coin_val)
    
data.sort(reverse = True) # 최대값부터 사용하기 위해 역정렬

cnt = 0

for coin in data:
    cnt += K // coin
    K %= coin
    
    if K <= 0:
        break
    
print(cnt)