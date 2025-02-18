from itertools import product


t = int(input())
while t > 0:
    t -= 1
    n = str(input())
    # flag = False
    # sum_digit = 0
    product_digit = 1
    for i in range(len(n)):
        # if i % 2 != 0:
        #     sum_digit += int(n[i])
        # else:
        if int(n[i]) != 0:
            flag = True
            product_digit *= int(n[i])
        else:
            product_digit *= 1
    
    print(product_digit)
    
    # if flag:
    #     print(product_digit, sum_digit)
    # else:
    #     print(0, sum_digit)