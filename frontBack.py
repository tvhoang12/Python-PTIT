t = int(input())
for i in range(t):
    n = str(input())
    if n[:2] == n[-2:]:
        print("YES")
    else:
        print("NO")