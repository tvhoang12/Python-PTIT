import math

if __name__ == "__main__":
    a, K, N = map(int, input().split())
    
    b = K - a % K + a
    
    list = []
    
    for i in range(b, N + 1, K):
        if i % K == 0:
            list.append(i - a)
    
    if len(list) == 0:
        print(-1)
    else:
        for i in list:
            print(i, end = " ")