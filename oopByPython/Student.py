from decimal import Rounded


class Student:
    def __init__(self, name, date_of_birth, sub1, sub2, sub3):
        self.name = name
        self.date_of_birth = date_of_birth
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def get_name(self):
        return self.name
    def get_date_of_birth(self):
        return self.date_of_birth
    def get_marks(self):
        return self.sub1 + self.sub2 + self.sub3
    
if __name__ == '__main__':
    name = input()
    date = input()
    sub1 = float(input())
    sub2 = float(input())
    sub3 = float(input())
    s = Student(name, date, sub1, sub2, sub3)
    print(s.get_name(), end = " ")
    print(s.get_date_of_birth(), end = " ")
    k = round(s.get_marks(), 2)
    print(k, end = " ")