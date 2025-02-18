

t = int(input())
while t > 0:
    t -= 1
    s = input().split(".")
    flag = True
    
    if len(s) != 4:
        flag = False
    else:
        for i in range(len(s)):
            if s[i].isdigit() == True:
                if int(s[i]) > 255 or int(s[i]) < 0:
                    flag = False
                    break
            else:
                flag = False
                break
    
    if flag == True:
        print("YES")
    else:
        print("NO")