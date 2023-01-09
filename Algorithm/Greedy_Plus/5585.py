N = int(input())
coin_type = [500, 100, 50, 10, 5, 1]

change = 1000 - N
result = 0

for coin in coin_type:
    if change == 0:
        break
    
    result += change // coin
    change %= coin
    
print(result)