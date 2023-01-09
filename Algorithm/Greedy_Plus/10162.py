# 내 정답
T = int(input())
button_type = [300, 60, 10]
button_cnt = [0, 0, 0]

result = 0

for i in range(len(button_type)):
    if T == 0:
        break
    
    button_cnt[i] = T // button_type[i]
    T %= button_type[i]
    
if 0 < T and T < button_type[-1]:
    print(-1)
else:
    print(' '.join([str(n) for n in button_cnt]))

# 다른 사람 정답
N = int(input())
A = N // 300
B = (N % 300) // 60
C = ((N % 300) % 60) // 10

if ((N % 300) % 60) % 10 != 0:
    print(-1)
else:
    print("{0} {1} {2}".format(A, B, C))