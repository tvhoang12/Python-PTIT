n = int(input())
a =[]
sumUp = 0
sumDown = 0
for i in range(n):
    k = list(map(int, input().split()))
    # k.reverse()
    a.append(k)

for i in range(n):
    for j in range(i + 1, n):
        sumUp += a[i][j]
        sumDown += a[j][i]

cd = int(input())

if abs(sumUp - sumDown) <= cd:
    print("YES")
else:
    print("NO")

print(abs(sumUp - sumDown))