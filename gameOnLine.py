from math import gcd


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    mp = {0:0}
    u = [0]
    
    for i in range(n):
        for j in u:
            d = gcd(a[i], j)
            cost = mp[j] + b[i]
            if d in mp:
                mp[d] = min(mp[d], cost)
            else:
                mp[d] = cost
                u.append(d)
    if 1 not in mp:
        mp[1] = -1
    print(mp[1])