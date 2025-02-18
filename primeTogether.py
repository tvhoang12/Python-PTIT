import math
import re

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    t -= 1
    n, m = map(int, input().split())
    k = str(math.gcd(n, m))
    res = 0
    for i in k:
        res += int(i)
    if isPrime(res):
        print('YES')
    else:
        print('NO')