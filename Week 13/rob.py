class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[-2] = nums[-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        return dp[0]
