arr = list(map(int, input().split()))
tot = sum(arr)
eq = tot // len(arr)
for i in range(1, len(arr)):
    if arr[i] < eq and arr[i-1] < arr[i]: