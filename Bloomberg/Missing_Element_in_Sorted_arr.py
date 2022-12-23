nums = list(map(int, input().split()))
k = int(input())

def solve(nums, k):
    n = len(nums)
    if n == 0: return k
    if k >= nums[n-1]:
        return k + nums[0] + n - 1
    
    i, num = 1, nums[0]
    while i < n and k > 0:
        num += 1
        if num == nums[i]:
            i += 1
        else:
            k -= 1
    return num + k

print(solve(nums, k))