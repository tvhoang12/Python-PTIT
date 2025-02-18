def isPrime(s):
    if s < 2:
        return False
    for i in range(2, int(s ** 0.5) + 1):
        if s % i == 0:
            return False
    return True

if __name__ == "__main__":
    n, x = [int(x) for x in input().split()]
    a = []
    a.append(x)
    s = 2
    
    while len(a) <= n:
        if isPrime(s):
            x += s
            a.append(x)
        s += 1
    
    print(*a)