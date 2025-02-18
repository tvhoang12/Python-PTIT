def check(m, s):
    for i in s:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n, m = map(int, input().split())
        k = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5":0, "6": 0, "7": 0, "8": 0, "9": 0}
        
        for i in range(n, m + 1):
            check(k, str(i))
        for i in k:
            print(k[i], end = ' ')
        print()