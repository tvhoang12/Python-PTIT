import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def shorten(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        return "{}/{}".format(self.numerator, self.denominator)
    
    def sumTwoFraction(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        gcd = math.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        return "{}/{}".format(numerator, denominator)

if __name__ == '__main__':
    arr = input().split()
    f1 = Fraction(int(arr[0]), int(arr[1]))
    f2 = Fraction(int(arr[2]), int(arr[3]))
    
    print(f1.sumTwoFraction(f2))
        
        