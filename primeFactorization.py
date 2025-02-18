import math

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = "1"
    cnt = 0
    
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt > 0:
            s += " * " + str(i) + "^" + str(cnt)
            cnt = 0
    if n > 1:
        s += " * " + str(n) + "^1"
    print(s)