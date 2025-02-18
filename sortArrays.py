t = int(input())
while t > 0:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    
    for i in range(n):
        if a[i] < 0:
            b.append(a[i])
    
    for i in range(n):
        if a[i] == max(a):
            b.append(k)
        if a[i] >= 0:
            b.append(a[i])
    
    for i in b:
        print(i, end = " ")
    print()