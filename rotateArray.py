t = int(input())
while t > 0:
    t -= 1
    n, d = map(int, input().split())
    lst = list(map(int, input().split()))
    tmp = lst[d:] + lst[:d]
    print(*tmp)