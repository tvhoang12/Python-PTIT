t = int(input())
while t > 0:
    t -= 1
    n, m, k = map(int, input().split())
    x, y, z = 0, 0, 0
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    lst = []
    
    while x < n and y < m and z < k:
        if a[x] == b[y] == c[z]:
            lst.append(a[x])
            x += 1
            y += 1
            z += 1
        elif a[x] < b[y]:
            x += 1
        elif b[y] < c[z]:
            y += 1
        else:
            z += 1
    if len(lst) == 0:
        print("NO")
    else:
        print(*lst, sep = " ", end = "\n")