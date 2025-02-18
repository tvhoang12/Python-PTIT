def fibonacci(f):
    f[1] = 1
    f[2] = 1
    for i in range(3, 94):
        f[i] = f[i - 1] + f[i - 2]
    
f = [0] * 95
fibonacci(f)
t = int(input())
while t > 0:
    t -= 1
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(f[i], end=" ")
    print()
    