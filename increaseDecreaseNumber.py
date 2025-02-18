def check(s):
    if len(s) < 3:
        return False
    if s[1] <= s[0] and s[-2] >= s[-1]:
        return False
    
    p1 = 1
    p2 = len(s) - 2
    
    while s[p1] > s[p1 - 1] and p1 < len(s) - 1:
        p1 += 1
    while s[p2] > s[p2 + 1] and p2 > 0:
        p2 -= 1
    if p1 == p2 + 2:
        return True
    else:
        return False

t = int(input())
for i in range(t):
    n = str(input())
    if check(n) == True:
        print("YES")
    else:
        print("NO")