n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 1
for i in range(n):
    if arr[i] - arr[i - 1] > m:
        cnt += 1

print(cnt)