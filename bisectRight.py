# upper bound in c
def bisectRight(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    target = int(input())
    print(bisectRight(arr, target)) 