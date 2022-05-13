from collections import deque
def sa(nums, k):
    dp = [0] * (len(nums) + 1)
    for i in range(1, len(dp)):
        dp[i] = dp[i - 1] + nums[i - 1]
    n = len(nums) + 1
    q = deque()

    for i in range(len(dp)):
        while q and dp[i] - dp[q[0]] >= k:
            n = min(n, i - q.popleft())
        while q and dp[i] < dp[q[-1]]:
            q.pop()
        q.append(i)
    return n if n != len(nums)+1 else -1

print(sa([1],1))
print(sa([1,2],4))
print(sa([2,-1,2],3))
