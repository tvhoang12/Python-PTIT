class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self._color = color[0].upper() + color[1::].lower()
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def color(self):
        return self._color

arr = input().split() 
if int(arr[0]) > 0 and int(arr[1]) > 0: 
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
    print("{} {} {}".format(r.perimeter(), r.area(), r.color())) 
else: 
    print("INVALID")