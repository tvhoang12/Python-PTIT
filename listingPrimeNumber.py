def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n = int(input())
lst = list(map(int, input().split()))

m = {}

for i in lst:
    if isPrime(i):
        if i not in m:
            m.update({i: 1})
        else:
            m[i] += 1
    else:
        pass

for i in m:
    print(i, m[i])