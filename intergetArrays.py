n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

a = list(a)
b = list(b)

anb = []
a_b = []
b_a = []

for i in a:
    if i not in b:
        a_b.append(i)
    else:
        anb.append(i)

b_a = [i for i in b if i not in a]

anb.sort()
a_b.sort()
b_a.sort()

for i in anb:
    print(i, end = ' ')
print()
for i in a_b:
    print(i, end = ' ')
print()
for i in b_a:
    print(i, end = ' ')