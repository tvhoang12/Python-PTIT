t = int(input())
while t > 0:
    t -= 1
    n, m = map(int, input().split())
    a = [[]]
    for i in range(n) :
        b = []
        while len(b) < m :
            b += list(map(int, input().split()))
        a.append(b)
    
    print(len(a))
    # for i in range(n):
    #     for j in range(n):
    #         s = 0
    #         for k in range(m):
    #             s += a[i][k] * a[j][k]
    #         print(s, end=' ')
    #     print()