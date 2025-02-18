import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n , m = map(int, input().split())
        k = math.gcd(n, m)
        
        x = 0
        while k >= 1:
            x += k % 10
            k = int(k / 10)
        
        if isPrime(x) == True :
            print("YES")
        else:
            print("NO")