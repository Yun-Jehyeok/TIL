N = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0

for i in range(0, N + 1):
    result += sum(data[:i])
    
print(result)