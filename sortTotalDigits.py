import functools

def projectDigits(n):
    total = 1
    s = str(n)
    for i in s:
        total *= int(i)
    return total
    

def cmp(a, b) :
    if projectDigits(a) == projectDigits(b) :
        if a > b : return 1
        else : return -1
    elif projectDigits(a) > projectDigits(b) : return 1
    else : return -1

t = int(input())
while t > 0:
    t -= 1
    j = int(input())
    lst = list(int(x) for x in input().split())
    lst = sorted(lst, key = functools.cmp_to_key(cmp))
    for i in lst:
        print(i, end=' ')
    print()