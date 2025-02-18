loca = [[-1 , -1],
        [0 , -1],
        [1 , -1],
        [-1 , 0],
        [1 , 0],
        [-1 , 1],
        [0 , 1],
        [1 , 1]]

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    q = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp)
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                q.append([i , j])
    cnt = 0
    while len(q) > 0:
        u = q.pop(0)
        for k in loca:
            x = u[0] + k[1]
            y = u[1] + k[0]
            if x >= 0 and x < n and y >= 0 and y < m:
                if a[x][y] != 0:
                    cnt += a[x][y]
                    a[x][y] = 0
                        
    print(cnt)