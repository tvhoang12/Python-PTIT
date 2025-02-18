def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
lst = list(map(int, input().split()))

location = [0] * n
prime = []

for i in range(n):
    if isPrime(lst[i]):
        location[i] = 1
        prime.append(lst[i])

prime.sort()
for i in range(n):
    if location[i] == 1:
        print(prime.pop(0), end = ' ')
    else:
        print(lst[i], end = ' ')