def subP(target, nums):
    total = left = right = 0
    mini = math.inf
    while right < len(nums):
        total += nums[right]
        while total >= target:
            total -= nums[left]
            left += 1
            mini = min(mini, right-left+2)
        right+=1
    return mini if mini != math.inf else 0
