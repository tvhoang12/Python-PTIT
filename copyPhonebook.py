class phonebook:
    def __init__(self, name, phoneNumber, date):
        self.name = name
        self.phoneNumber = phoneNumber
        self.date = date
        self.x = name.split()[-1]
    def generatePhonebook(self):
        return self.name + ': ' + self.phoneNumber + ' ' + self.date

if __name__ == "__main__":
    pb = open('SOTAY.txt', 'r')
    ip = pb.read().split('\n')
    
    a = []
    while len(ip) > 0:
        x = ip.pop(0)
        if x[:4:] == "Ngay": date = x[5::]
        elif len(ip) > 0:
            a.append(phonebook(x, ip.pop(0), date))
    a = sorted(a, key=lambda x: (x.x, x.name))
    pb.close()
    ot = open('DIENTHOAI.txt', 'w')
    for i in a:
        ot.write(i.generatePhonebook() + '\n')
    ot.close()
    
    
    