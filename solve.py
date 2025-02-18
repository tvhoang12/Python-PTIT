P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    ip = input()
    if ip == "0":
        break
    k, s = ip.split()
    
    k = int(k)
    n = ""
    for i in s:
        x = 0
        for j in range(len(P)):
            if i == P[j]:
                x = j
                break
            x += 1
        x = (x + k) % 28
        n = P[x] + n
    
    print(n)