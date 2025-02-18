import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isPrimeDigit(n):
    if n == '2' or n == '3' or n == '5' or n == '7':
        return True
    return False

def check(s):
    for i in range(len(s)):
        if isPrime(i) and isPrimeDigit(int(s[i])):
            continue
        elif isPrime(i) == False and isPrimeDigit(int(s[i])) == False:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        if check(s) == True:
            print("YES")
        else:
            print("NO")
