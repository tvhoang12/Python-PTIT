import math
comb = []

def initCombination(a):
    for i in range(0, 3):
        comb.append(a + i)

def nextCombination(n, flag_list):
    # print("++")
    i = 2
    flag = flag_list[0]
    while i >= 0 and comb[i] == n - 2 + i:
        i -= 1
    if i == -1:
        flag_list[0] = False
    else:
        comb[i] += 1
        for j in range(i + 1, 3):
            comb[j] = comb[j - 1] + 1

def checkPrimeTogether():
    if math.gcd(comb[0], comb[1]) == 1 and math.gcd(comb[1], comb[2]) == 1 and math.gcd(comb[0], comb[2]) == 1:
        return True
    else :
        return False

if __name__ == "__main__":
    a, b = map(int, input().split())
    initCombination(a)
    flag_list = [True]
    while flag_list[0] == True:
        if checkPrimeTogether():
            print("(", comb[0], ", " ,comb[1], ", " ,comb[2], ")", sep = "" )
        nextCombination(b, flag_list)