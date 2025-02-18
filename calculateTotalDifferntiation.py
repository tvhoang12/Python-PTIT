import math

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        suma = 0.0
        for j in range(2 - n % 2, n + 1, 2):
            suma += 1.0 / j
        print("%.6f" % suma)