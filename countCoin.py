t = int(input())
a = [""] * t
for i in range(t):
    a[i] = input()

b = [0] * t
c = [0] * t
s = 0

for i in range(t):
    for j in range(t):
        if a[i][j] == 'C':
            b[i] += 1
            c[j] += 1

for i in range(t):
    s += b[i] * (b[i] - 1) // 2
    s += c[i] * (c[i] - 1) // 2

print(s)