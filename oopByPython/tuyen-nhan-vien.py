class nhanvien:
    def __init__(self,ms, ten, lythuyet, thuchanh):
        self.ms = ms
        self.ten = ten
        self.lythuyet = lythuyet
        self.thuchanh = thuchanh
    
    def trungbinh(self):
        return (self.lythuyet + self.thuchanh) / 2
    
    def phanloai(self):
        if self.trungbinh() < 5:
            return 'TRUOT'
        elif self.trungbinh() < 8:
            return 'CAN NHAC'
        elif self.trungbinh() < 9.5:
            return 'DAT'
        else:
            return 'XUAT SAC'
        
if __name__ == "__main__":
    t = int(input())
    s = []
    for i in range(1, t + 1):
        ms = i
        ten = input()
        lythuyet = float(input())
        thuchanh = float(input())
        if lythuyet > 10:
            lythuyet /= 10
        if thuchanh > 10:
            thuchanh /= 10
        s.append(nhanvien(ms, ten, lythuyet, thuchanh))
    
    s.sort(key = lambda k : -k.trungbinh())
    for i in s:
        print(f"TS0{i.ms} {i.ten} {i.trungbinh():.2f} {i.phanloai()}")
        