t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    lst = list(map(int, input().split()))
    m = {-1:-1}
    m.pop(-1)
    lst.sort()
    
    for i in range(n):
        if lst[i] in m:
            m[lst[i]] += 1
        else:
            m[lst[i]] = 1
    
    for i in m:
        if m[i] % 2 == 1:
            print(i)
            break