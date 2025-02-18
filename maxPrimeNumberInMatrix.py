def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
arr = []
Max = -1
for i in range(n):
    s = list(map(int, input().split()))
    arr.append(s)
    for i in s:
        if isPrime(i):
            Max = max(Max, i)

if Max == -1:
    print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == Max:
                print("Vi tri [" , i , "][" , j , "]", sep = "")