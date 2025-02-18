t = int(input())
while t >= 1:
    t -= 1
    s = str(input())
    rever_s = s[::-1]
    flag = True
    
    for i in range(len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(rever_s[i]) - ord(rever_s[i - 1])):
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")