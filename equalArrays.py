n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

a = list(a)
b = list(b)

if len(a) != len(b):
    print('NO')
else:
    a.sort()
    b.sort()
    # flag = True
    for i in range(len(a)):
        if a[i] != b[i]:
            print('NO')
            break
    else:
        print('YES')