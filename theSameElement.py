t = int(input())
while t > 0:
    t -= 1
    
    n = int(input())
    x, y, z = map(int, input().split())
    s = (1, 1)
    Min = 1000000000
    qu = []
    qu.append(s)
    
    while len(qu) > 0:
        s = qu[0]
        qu.pop(0)
        
        if s[0] == n:
            Min = min(Min, s[1])
            
        else:
            if s[0] > n:
                new_s = (s[0] - y, s[1] + y)
                qu.append(new_s)
            elif s[0] < n:
                qu.append((s[0] + x, s[1] + x))
                qu.append((s[0] * z, s[1] + z))
    print(Min)