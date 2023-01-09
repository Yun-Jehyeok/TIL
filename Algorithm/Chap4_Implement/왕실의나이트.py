# 내 정답
data = input()

x = data[0]
y = int(data[1])

x_path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
plans = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

cnt = 0

for plan in plans:
    nx = x_path.index(x) + plan[0]
    ny = y + plan[1]
    
    if nx >= 0 and ny >= 1 and nx <= 7 and ny <= 8:
        cnt += 1
        
print(cnt)