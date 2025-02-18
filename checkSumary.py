if __name__ == "__main__":
    while True:
        s = input()
        if s == "-1":
            break
        else:
            x, y = s.split()
            x = int(x)
            y = int(y)
            z = int(input())
            cnt = 0
            
            for i in range(x, y + 1):
                check = True
                for j in range(2, z + 1):
                    if i % j == 0:
                        check = False
                        break
                if check:
                    cnt += 1
                else:
                    continue
            print(cnt)
