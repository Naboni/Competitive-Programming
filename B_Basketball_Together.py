n, m = map(int, input().split())
arr = list(map(int, input().split()))

l,r = 0,len(arr) - 1
cnt = 0
arr.sort()
summ = 0
while l <= r:
    summ += arr[r]
    if summ > m:
        summ = 0
        cnt += 1
        r -= 1
    else:
        l += 1
        
print(cnt)