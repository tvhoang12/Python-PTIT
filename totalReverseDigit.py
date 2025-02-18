def totalDigit(n):
    sum_digit = 0
    for i in range(len(n)):
        sum_digit += int(n[i])
    return sum_digit

def checkReversal(n):
    if len(n) <= 1:
        return False
    else:
        s = n[::-1]
        for i in range(0, len(n) // 2 + 1):
            if int(n[i]) % 2 != 0:
                return False
        if n == s:
            return True
        else:
            return False

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        for i in range(22, n, 2):
            if checkReversal(str(i)):
                print(i, end=" ")
        print()
        t -= 1