s = str(input())

n = len(s)
if n % 2 == 1:
    n -= 1

lst = [-1]
lst.remove(-1)
for i in range(0, n, 2):
    if int(s[i:i+2]) not in lst:
        lst.append(int(s[i:i+2]))

print(*lst)
