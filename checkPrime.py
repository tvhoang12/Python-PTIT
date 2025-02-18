import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
m = []
for i in range(n):
    a = list(map(int, input().split()))
    m.append(a)

for i in m:
    for j in i:
        if isPrime(j):
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()