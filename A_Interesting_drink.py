n = int(input())
prices = list(map(int, input().split()))
q = int(input())

prices.sort()
def binarySearch(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left


for _ in range(q):
    m = int(input())
    print(binarySearch(prices, m))