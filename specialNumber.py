if __name__ == "__main__":
    t = int(input())
    mod = 10 ** 9 + 7
    while t > 0:
        t -= 1
        n, m = map(int, input().split())
        res, tmp = 0, 1
        while m > 0:
            if m & 1 == 1:
                res = (res + tmp) % mod
            tmp = (tmp * n) % mod
            m >>= 1
        print(res)
        
        