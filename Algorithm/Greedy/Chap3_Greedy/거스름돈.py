N = int(input())
coin_list = [500, 100, 50, 10]
count = 0

for coin in coin_list:
	count += N // coin
	N %= coin

print(count)