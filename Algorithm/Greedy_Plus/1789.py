S = int(input())

num = 0

while S > num:
    num += 1
    S -= num
    
print(num)