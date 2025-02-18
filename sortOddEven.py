n = int(input())
a = 0
s = []
while True:
    lst = list(map(int, input().split()))
    s += lst
    if len(s) == n:
        break

location = [0]*n
lst_odd = []
lst_even = []

for i in range(n):
    if s[i] % 2 == 0:
        lst_even.append(s[i])
    else:
        location[i] = 1
        lst_odd.append(s[i])

lst_even.sort()
lst_odd.sort(reverse = True)

for i in range(n):
    if location[i] == 1:
        print(lst_odd.pop(0), end = " ")
    else:
        print(lst_even.pop(0), end = " ")