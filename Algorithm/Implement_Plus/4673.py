data1 = set(range(1, 10001))
data2 = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    
    data2.add(i)
        
result = sorted(data1 - data2)

for i in result:
    print(i)