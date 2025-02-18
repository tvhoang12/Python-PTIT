n = int(input())
lst = list(map(int, input().split()))
lst.sort()

std = 1

std = max(lst[-1] * lst[-2] * lst[-3], lst[0] * lst[1] * lst[-1])

print(std)