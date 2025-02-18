from os import name


class student:
    def __init__(self,id, name, score, type):
        self.id = id
        self.name = name
        self.score = score
        self.type = type
    
    def get_type(self):
        return self.type

if __name__ == '__main__':
    t = int(input())
    id = 0
    s = []
    while t > 0:
        t -= 1
        id += 1
        name = input()
        score = [float(x) for x in input().split()]
        score[0] = score[0] * 2
        score[1] = score[1] * 2
        score = sum(score) / 12
        if score < 5:
            type = "YEU"
        elif score >= 5 and score < 7:
            type = "TB"
        elif score >= 7 and score < 8:
            type = "KHA"
        elif score >= 8 and score < 9:
            type = "GIOI"
        else:
            type = "XUAT SAC"
        st = student(id, name, score, type)
        
        s.append(st)
    
    s.sort(key=lambda x: x.score, reverse=True)
    for i in range(len(s)):
        stu = s[i]
        print(f"HS{stu.id:02} {stu.name} {round(stu.score + 0.01, 1)} {stu.get_type()}" )
        