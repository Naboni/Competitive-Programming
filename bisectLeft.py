def bisectLeft(arr, target):
    left, right =  0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
arr = list(map(int, input().split()))
target = int(input())
print(bisectLeft(arr, target))