n, m = map(int, input().split())
Max = -1
Min = 1000000000000
lst = []

for i in range(n):
    s = list(map(int, input().split()))
    lst.append(s)
    Max = max(Max, max(s))
    Min = min(Min, min(s))

k = Max - Min
flag = False
for i in lst:
    if k in i:
        flag = True
        break
    
if flag == False:
    print("NOT FOUND")
else:
    print(k)
    for i in range(n):
        for j in range(m):
            if lst[i][j] == k:
                print("Vi tri [" , i , "][" , j , "]", sep = "")
                flag = True
