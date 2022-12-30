arr = list(map(int, input().split()))
k = int(input())

def solve(arr, k):
    left = right = 0
    summ = 0
    for right in range(k):
        summ += arr[right]
    res = [summ, [left, right]]
    for right in range(k, len(arr)):
        summ += arr[right]
        summ -= arr[left]
        left += 1
        if summ < res[0]:
            res[1] = [left, right]
            res[0] = summ
    return res[1]

print(*solve(arr, k))