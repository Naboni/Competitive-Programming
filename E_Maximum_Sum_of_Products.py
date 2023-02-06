n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

summ = 0
for i in range(n):
    summ += arr1[i] * arr2[i]
res = summ

for i in range(0, n-1):
    left, right = i, i+1
    diff = 0
    while left >= 0 and right < n:
        diff += (arr1[left] - arr1[right]) * (arr2[right] - arr2[left])
        res = max(res, summ + diff)
        left -= 1
        right += 1

for i in range(1, n-1):
    left, right = i-1, i+1
    diff = 0
    while left >= 0 and right < n:
        diff += (arr1[left] - arr1[right]) * (arr2[right] - arr2[left])
        res = max(res, summ + diff)
        left -= 1
        right += 1

print(res)