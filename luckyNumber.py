import math

def luckyNumber(n):
    for i in range(len(n)):
        if n[i] != '4' and n[i] != '7':
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    while t >= 1:  
        n = str(input())
        if luckyNumber(n):
            print("YES")
        else:
            print("NO")
        t -= 1