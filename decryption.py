if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = str(input())
        tmp = ""
        for i in range(0, len(s) - 1, 2):
            for j in range(int(s[i + 1])):
                tmp += s[i]
        
        print(tmp)
            