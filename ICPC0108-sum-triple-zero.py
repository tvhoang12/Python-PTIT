t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    res = 0

    for i in range(len(lst)):
        l = i + 1
        r = n - 1
        while l < r:
            if lst[i] + lst[r] + lst[l] == 0:
                l += 1
                res += 1
            elif lst[i] + lst[r] + lst[l] < 0:
                l += 1
            else:
                r -= 1

    print(res)