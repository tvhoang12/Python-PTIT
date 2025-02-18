def rotate(s):
    d = 0
    x = ''
    for i in s:
        d += ord(i) - ord('A')
    for i in s:
        x += chr((ord(i) - ord('A') + d) % 26 + ord('A'))
    return x

t = int(input())
while t > 0:
    t -= 1
    s, x = input(), ''
    
    n = int(len(s) / 2)
    
    a, b = s[:n:], s[n::]
    a = rotate(a)
    b = rotate(b)
    
    for i in range(int(n)):
        x += chr((ord(a[i]) - ord('A') + ord(b[i]) - ord('A')) % 26 + ord('A'))
    print(x)