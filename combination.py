

def combinationGenerator(a, b):
    global n, k
    if len(b) == k:
        print(*b)
        return
    
    for i in range(a, n):
        combinationGenerator(i + 1, b + [list[i]])
        
n, k = map(int, input().split())
list = sorted(list({int(i) for i in input().split()}))
n = len(list)

combinationGenerator(0, [])