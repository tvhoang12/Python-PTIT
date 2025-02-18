def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    lst = list(map(int, input().split()))
    lst_2 = []
    
    for i in lst:
        if i not in lst_2:
            lst_2.append(i)
        else:
            pass
    
    total_right = sum(lst_2)
    total_left = 0
    flag = False
    
    for i in range(len(lst_2)):
        total_left += lst_2[i]
        total_right -= lst_2[i]
        if isPrime(total_left) and isPrime(total_right):
            print(i)
            flag = True
            break
    
    if not flag:
        print("NOT FOUND")