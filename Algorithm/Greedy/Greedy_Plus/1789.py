S = int(input())

num = 0
cnt = 0

while S > num:
    num += 1
    S -= num
    
    cnt += 1

print(cnt)