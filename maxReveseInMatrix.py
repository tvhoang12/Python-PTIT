def reverse(s):
    if len(s) > 1 and s == s[::-1]:
        return True
    return False

n, m = map(int, input().split())
arr = []
Max = -1

for i in range(n):
    s = list(map(int, input().split()))
    arr.append(s)
    for i in s:
        if reverse(str(i)):
            Max = max(Max, i)

if Max == -1:
    print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == Max:
                print("Vi tri [" , i , "][" , j , "]", sep = "")