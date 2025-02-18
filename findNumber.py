t = int(input())
while t > 0:
    t -= 1
    s = str(input())
    s += 'z'
    n = 0
    lst = []
    
    for i in range(0, len(s)):
        if s[i].isalpha():
            if i != 0 and s[i-1].isdigit():
                lst.append(int(n))
            n = 0
        else:
            n = n * 10 + int(s[i])
    
    print(max(lst))
            