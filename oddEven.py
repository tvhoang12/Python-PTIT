if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = str(input())
        sum = 0
        ok = False
        for i in range(len(s) - 1):
            sum += int(s[i])
            if abs(int(s[i]) - int(s[i + 1])) != 2:
                break
        if (sum + int(s[len(s) - 1])) % 10 == 0:
            ok = True
        if ok:
            print("YES")
        else:
            print("NO")