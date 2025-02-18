n = int(input())
lst = []
x = 0
Max = -1
flag = False

while True:
    tmp = list(map(int, input().split()))
    x += len(tmp)
    lst = lst + tmp
    Max = max(Max, max(tmp))
    if x == n:
        break

for i in range(1, Max):
    if i not in lst:
        flag = True
        print(i)

if flag == False:
    print("Excellent!")