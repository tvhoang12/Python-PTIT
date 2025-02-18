m, n = map(int, input().split())
a = list(map(int, input().split()))

b = {-1:-1}
b.pop(-1)
ans, x, s = 0, 0, 0

for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
    s = max(s, b[i])

for i in range(1, n + 1):
    if i in b and b[i] != s and b[i] > x:
        x = b[i]
        ans = i
if ans == 0:
    print("NONE")
else:
    print(ans)