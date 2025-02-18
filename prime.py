import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

lst = ["2", "3", "5", "7"]

def check(n):
    if n in lst:
        return True
    else:
        return False
    
def totalPrime(n):
    cnt = 0
    for i in range(len(n)):
        if check(n[i]) == True:
            cnt += 1
    return cnt > int(len(n) - cnt)

t = int(input())
while t > 0:
    t -= 1
    s = input()
    if isPrime(int(len(s))) and totalPrime(s):
        print("YES")
    else:
        print("NO")