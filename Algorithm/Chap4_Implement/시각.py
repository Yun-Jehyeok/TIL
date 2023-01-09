# 내 정답
N = int(input())

cnt = 0

for i in range((N + 1) * 60 * 60):
    s = str(i % 60)
    m = str(i % 3600 // 60)
    h = str(i // 3600)
    
    if '3' in h + m + s:
        cnt += 1
        
print(cnt)

# 답안
h = int(input())

cnt = 0

for i in range(h + 1):
	for j in range(60):
		for k in range(60):
			if '3' in str(i) + str(j) + str(k):
				cnt += 1

print(cnt)