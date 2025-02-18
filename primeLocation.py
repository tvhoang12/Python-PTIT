import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    t -= 1
    s = str(input())
    flag = True
    
    for i in range(len(s)):
        if isPrime(int(i)) != isPrime(int(s[i])):
            flag = False
            break
    
    if flag == True:
        print("YES")
    else:
        print("NO")