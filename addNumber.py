t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    
    for i in range(min(a), max(a)):
        if not(i in a):
            cnt += 1
    
    print(cnt)