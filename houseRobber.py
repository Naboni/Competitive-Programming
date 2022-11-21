n = int(input())
nums = list(map(int, input().split()))

# Top Down, TC: O(N) SC: O(N) + O(N) (Recursion stack with dp array)
dp1 = [-1] * n
def topDown(idx):
    if idx == n-1: return nums[idx]
    if idx >= n: return 0
    if dp1[idx] != -1: return dp1[idx]

    pick = nums[idx] + topDown(idx+2)
    not_pick = topDown(idx+1)
    return max(pick, not_pick)

# print(topDown(0))

# Top Down, TC: O(N) SC: O(N)
def bottomUp():
    dp2 = [-1] * n
    dp2[-1] = nums[-1]
    for i in range(n-2, -1, -1):
        pick = nums[i]
        if i+2 < n:
            pick += dp2[i+2]
        not_pick = dp2[i+1]
        dp2[i] = max(pick, not_pick)    
    return dp2[0]

# print(bottomUp())

# Top Down, TC: O(N) SC: O(1)
def bottomUpWithTabulation():
    prev = nums[-1]
    prev2 = 0

    for i in range(n-2, -1, -1):
        pick = nums[i]
        if i+2 < n:
            pick += prev2
        not_pick = prev
        curr = max(pick, not_pick)
        prev, prev2 = curr, prev
    return prev

print(bottomUpWithTabulation())