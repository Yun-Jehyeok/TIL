data = str(input())

cntFor0 = 0 # 1 -> 0
cntFor1 = 0 # 0 -> 1

if data[0] == '0':
    cntFor1 = 1
else:
    cntFor0 = 1
    
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i] == '0':
            cntFor1 += 1
        else:
            cntFor0 += 1
            
print(min(cntFor0, cntFor1))