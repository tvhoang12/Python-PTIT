x = 0
m = {-1}
while True:
    s = [int(x) for x in input().split()]
    x += len(s)
    for i in s:
        m.add(i % 42)
    if x == 10:
        break
print(len(m) - 1)
