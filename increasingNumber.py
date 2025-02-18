def increasingNumber(n):
    for i in range(len(n) - 1):
        if int(n[i]) > int(n[i + 1]):
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = str(input())
        if increasingNumber(s):
            print("YES")
        else:
            print("NO")     