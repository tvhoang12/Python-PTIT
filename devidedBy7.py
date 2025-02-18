
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        s = str(input())
        cnt = 0
        sum_check = int(s)
        while cnt < 1000 and sum_check % 7 != 0:
            cnt += 1
            sum_check += int(str(sum_check)[::-1])
        if cnt == 1000:
            print(-1)
        else:
            print(sum_check)
        