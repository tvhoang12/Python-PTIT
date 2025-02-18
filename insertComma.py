if __name__ == "__main__":
    n = str(input())
    k = ""
    tmp = -2
    for i in range(len(n)):
        k = n[-i - 1] + k
        if tmp % 3 == 0:
            k = "," + k
        tmp += 1
    
    print(k.strip(","))