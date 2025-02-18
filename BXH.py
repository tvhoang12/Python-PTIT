import functools

class Student:
    def __init__(self, name, Ac, Submit):
        self.name = name
        self.Ac = Ac
        self.Submit = Submit

def cmp(a, b):
    if a.Ac < b.Ac: return 1
    elif a.Ac == b.Ac:
        if a.Submit > b.Submit: return 1
        elif a.Submit == b.Submit:
            if a.name > b.name: return 1
            else: return -1
        else: return -1
    else: return -1
    
if __name__ == "__main__":
    t = int(input())
    s = []
    while t > 0:
        t -= 1
        
        name = input()
        Ac, Submit = map(int, input().split())
        s.append(Student(name, Ac, Submit))
    
    s = sorted(s, key = functools.cmp_to_key(cmp))
    
    for i in s:
        print(i.name, i.Ac, i.Submit)