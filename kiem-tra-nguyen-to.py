import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n, m = map(int, input().split())
lst = [[0] * m for i in range(n)]

for i in range(n):
    lst[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if isPrime(lst[i][j]):
            lst[i][j] = 1
        else:
            lst[i][j] = 0

for i in range(n):
    print(*lst[i])