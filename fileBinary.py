base_8 = {
    "000":0,
    "001":1,
    "010":2,
    "011":3,
    "100":4,
    "101":5,
    "110":6,
    "111":7,
}
base_4 = {
    "00":0,
    "01":1,
    "10":2,
    "11":3,
}

base_16 = {
    "0000":0,
    "0001":1,
    "0010":2,
    "0011":3,
    "0100":4,
    "0101":5,
    "0110":6,
    "0111":7,
    "1000":8,
    "1001":9,
    "1010":"A",
    "1011":"B",
    "1100":"C",
    "1101":"D",
    "1110":"E",
    "1111":"F",
}

def change_to_base_8(s):
    while len(s) % 3 != 0:
        s = "0" + s
    k = ""
    for i in range(0, len(s), 3):
        k = k + str(base_8[s[i:i+3]])
    
    return k

def change_to_base_4(s):
    while len(s) % 2 != 0:
        s = "0" + s
    k = ""
    for i in range(0, len(s), 2):
        k = k + str(base_4[s[i:i+2]])
    
    return k

def change_to_base_16(s):
    while len(s) % 4 != 0:
        s = "0" + s
    k = ""
    for i in range(0, len(s), 4):
        k = k + str(base_16[s[i:i+4]])
    
    return k

if __name__ == '__main__':
    file = open('DATA.in', 'r')
    t = int(file.readline())
    while t > 0:
        t -= 1
        n = int(file.readline())
        s = file.readline().rstrip('\n')
        
        if n == 2:
            print(s)
        elif n == 4:
            print(change_to_base_4(s))
        elif n == 8:
            print(change_to_base_8(s))
        elif n == 16:
            print(change_to_base_16(s))