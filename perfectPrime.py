import math

def sumDigit(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

def isPrime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def isPerfectPrime(n):
    if isPrime(n):
        reverse_n = int(str(n)[::-1])
        if isPrime(sumDigit(n)) and isPrime(reverse_n):
            return True
    return False

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        
        if isPerfectPrime(n):
            print("Yes")
        else:
            print("No")