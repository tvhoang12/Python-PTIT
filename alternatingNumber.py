if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        n = str(input())
        flag = True
        cnt = n[0]
        if int(len(n)) % 2 != 0 and n[0] != n[1]:
            for i in range(len(n)):
                if i % 2 == 0 and n[i] != n[0]:
                        flag = False
                        break
        else:
            flag = False
        
        if flag == True:
            print("YES")
        else:
            print("NO")