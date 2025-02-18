t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    s = 0
    
    for i in range(len(lst)):
        l = i + 1
        r = len(lst) - 1
        while l < r:
            if lst[l] + lst[r] + lst[i] == 0:
                l += 1
                s += 1
            elif lst[l] + lst[r] + lst[i] > 0:
                r -= 1
            else:
                l += 1
    print(s)