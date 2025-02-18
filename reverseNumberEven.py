a = []
b = ["0","2", "4", "6", "8"]

def gen(s):
    a.append(int(s + s[::-1]))
    if len(s) < 3:
        for i in b:
            gen(s + i)

gen("2")
gen("4")
gen("6")
gen("8")

a.sort()

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in a:
        if i < n:
            print(i, end = " ")
        else:
            break
    print()