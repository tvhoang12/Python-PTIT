def checkLocPhat(s):
    if s[0] != '6':
        return False
    for i in range(len(s)):
        if s[i] != '8' and s[i] != '6':
            return False
        if i >= 2 and s[i - 2: i + 1:] == '888':
            return False
        
    return True


if __name__ == '__main__':
    s = str(input())
    if checkLocPhat(s):
        print("YES")
    else:
        print("NO")