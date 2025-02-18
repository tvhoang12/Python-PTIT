a = []
b = ["0","1", "2"]
def checkTriplet(s):
    cnt = 0
    for i in s:
        if i == '2':
            cnt += 1
    
    if cnt > len(s) / 2: return True
    else: return False

def generateTriplet(s):
    if checkTriplet(s):
        a.append(s)
    if len(s) < 10:
        for i in b:
            generateTriplet(s + i)

generateTriplet("1")
generateTriplet("2")

a = sorted([int(x) for x in a])
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(n):
        print(a[i], end = " ")
    print()