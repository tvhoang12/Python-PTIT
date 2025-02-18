def reverseNummber(n):
    n = str(n)
    n = n[::-1]
    return int(n)

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        if n <= 12:
            print()
        else:
            m = []
            for i in range(13, n):
                    if reverseNummber(i) < n and isPrime(i) and isPrime(reverseNummber(i)) and i < reverseNummber(i):
                        m.append(i)
                        m.append(reverseNummber(i))
                        print(i, reverseNummber(i), end = ' ')
            print()