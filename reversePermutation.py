def next_permutation(L):
    n = len(L)

    # Step 1: find rightmost position i such that L[i] < L[i+1]
    i = n - 2
    while i >= 0 and L[i] >= L[i+1]:
        i -= 1

    if i == -1:
        return False  # L is the last permutation

    # Step 2: find rightmost position j to the right of i such that L[j] > L[i]
    j = n - 1
    while L[j] <= L[i]:
        j -= 1

    # Step 3: swap L[i] and L[j]
    L[i], L[j] = L[j], L[i]

    # Step 4: reverse everything to the right of i
    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        
        a = [[]]
        
        n = int(input())
        k = []
        
        for i in range(n):
            k.append(i + 1)
        
        a.append(k[:])
        
        while next_permutation(k):
            a.append(k[:])
        
        print(len(a) - 1)
        for i in range(len(a) - 1, 0, -1):
            print(*a[i], sep = "", end = " ")
        print()
        