while True:
    n = int(input())
    if n == 0:
        break
    biggest = -1
    smallest = 10**100
    while n > 0:
        n -= 1
        x = int(input())
        biggest = max(biggest, x)
        smallest = min(smallest, x)
    if biggest == smallest:
        print("BANG NHAU")
    else:
        print(smallest, biggest, sep = " ", end = "\n")
    
        