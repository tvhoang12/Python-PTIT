s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def backtrack(n, k):
    if k == 2**(n - 1):
        return s[n - 1]
    elif k < 2**(n - 1):
        return backtrack(n - 1, k)
    else:
        return backtrack(n - 1, k - 2**(n - 1))
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        print(backtrack(n, k))
