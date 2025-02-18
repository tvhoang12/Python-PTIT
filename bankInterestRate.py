import math

if __name__ == "__main__":
    t = int(input())
    while t >= 1:  
        N, X, M = map(float, input().split())
        x = (X + 100) / 100
        s = math.log(M/N, x)
        if s != int(s):
            s = int(s) + 1
        print(int(s))
        t -= 1