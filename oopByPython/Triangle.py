from decimal import Decimal
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        f = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2).sqrt()
        return f

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2 
        self.p3 = p3
    
    def checkTriangle(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        
        if max(a, b, c) * 2 >= a + b + c:
            print("INVALID")
        else:
            d = math.sqrt((a + b + c) * (a + b - c) * (b + c - a) * (c + a - b)) / 4
            print("{:.2f}".format(d))
            
arr = []
t = int(input())
for x in range(t):
    arr += list(map(float, input().split()))
i = 0
for index in range(t):
    p1 = Point(Decimal(arr[i]), Decimal(arr[i + 1]))
    p2 = Point(Decimal(arr[i + 2]), Decimal(arr[i + 3]))
    p3 = Point(Decimal(arr[i + 4]), Decimal(arr[i + 5]))
        
    Tria = Triangle(p1, p2, p3)
    Tria.checkTriangle()
    i += 6