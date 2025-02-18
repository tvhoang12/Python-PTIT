t = int(input())
while t > 0:
    t -= 1
    s = str(input())
    n = str(input())
    print(len(s.split(n)) - 1)
    