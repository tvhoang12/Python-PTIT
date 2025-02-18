def checkReverse(s):
    if s == s[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    file = open("VANBAN.in", "r")
    b = {}
    cnt = 0
    for line in file:
        a = line.split()
        for i in a:
            if checkReverse(i):
                if len(i) > cnt:
                    cnt = len(i)
                    b.clear()
                    b[i] = 1
                elif len(i) == cnt:
                    if i in b:
                        b[i] += 1
                    else:
                        b[i] = 1
    for i in b:
        print(i, b[i])