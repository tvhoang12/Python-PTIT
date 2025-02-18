t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    lst_1 = list(map(int, input().split()))
    lst_2 = list(map(int, input().split()))
    flag  = True
    lst_1.sort()
    lst_2.sort()
    
    for i in range(n):
        if lst_1[i] > lst_2[i]:
            flag = False
            break
        
    if flag:
        print("YES")
    else:
        print("NO")