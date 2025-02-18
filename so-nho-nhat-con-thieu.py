t = int(input())
lst = list(map(int, input().split()))

for i in range(1, max(lst) + 2):
    if i not in lst:
        print(i)
        break