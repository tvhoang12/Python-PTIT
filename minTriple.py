t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    lst = list(map(int, input().split()))
    sum = 0
    
    for i in range(3):
        sum += min(lst)
        lst.remove(min(lst))
    
    print(sum)