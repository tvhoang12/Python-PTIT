lst = []
for t in range(int(input())):
    tmp = input()
    if tmp != '':
        lst += [tmp]
    else:
        print(f'{lst[0]}: {len(lst) - 1}')
        lst.clear()
print(f'{lst[0]}: {len(lst) - 1}')