t = int(input())
while t > 0:
    t -= 1
    n, m = map(int, input().split())
    s = input().strip()
    if(s.count(" ")): s, k = s.split()
    else: k = input()

    p = str(min(n, m))
    q = str(max(n, m))
    
    print(int(s.replace(q, p)) + int(k.replace(q, p)), end=" ")
    print(int(s.replace(p, q)) + int(k.replace(p, q)))