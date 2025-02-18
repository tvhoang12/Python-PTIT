t = int(input())
for i in range(t):
    n = str(input())
    k = int(len(n))
    for i in range(k):
        if int(n[i]) >= 5:
            n[i - 1] = int(n[i - 1]) + 1
            n[i] = int(0)
        else:
            n[i] = int(0)
    print(n)