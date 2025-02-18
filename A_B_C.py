def tryABC(s, n, a, b, c):
    if len(s) == n and a <= b and b <= c and a > 0:
        print(s)
    if len(s) < n:
        tryABC(s + "A", n, a + 1, b, c)
        tryABC(s + "B", n, a, b + 1, c)
        tryABC(s + "C", n, a, b, c + 1)

t = int(input())
for i in range(3, t + 1):
    tryABC("", i, 0, 0, 0)