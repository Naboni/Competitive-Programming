t = int(input())
def bisectRight(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def solve(n, q, hei, que):
    arr = [hei[0]]
    for a in hei[1:]:
        arr.append(max(a, arr[-1]))
    height = [hei[0]]
    for a in hei[1:]:
        height.append(a+height[-1])
    ans = []
    for q in que:
        i = bisectRight(arr, q)
        if i==0:
            ans.append(0)
        else:
            ans.append(height[i-1])
    return ans

for _ in range(t):
    n, q = map(int, input().split())
    height = list(map(int, input().split()))
    que = list(map(int, input().split()))
    print(*solve(n, q, height, que))