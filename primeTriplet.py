def isPrime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    lst = [5, 7, 11]
    cnt = 0
    if n < 11:
        print(cnt)
    else:
        for i in range(13, n + 1, 2):
            if isPrime(i):
                lst.append(i)
        for i in range(len(lst) - 2):
            if lst[i] + 2 == lst[i + 1] and lst[i] + 6 == lst[i + 2]:
                cnt += 1
            elif lst[i] + 4 == lst[i + 1] and lst[i] + 6 == lst[i + 2]:
                cnt += 1
        print(cnt)