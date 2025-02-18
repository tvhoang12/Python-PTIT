import math

n = int(input())
d = 0

for i in range(1, n):
    if i != math.pow(int(math.sqrt(i)), 2):
        continue
    else:
        cnt = 0
        for j in range(1, int(math.sqrt(i))):
            if i % j == 0:
                cnt += 1
        
        if cnt == 4:
            d += 1

print(d)