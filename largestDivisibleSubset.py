class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1]*n
        nums.sort()
        maxi = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    maxi = max(maxi, dp[i])
        prev = -1
        res = []
        for i in range(n-1, -1, -1):
            if dp[i] == maxi and (prev % nums[i] == 0 or prev == -1):
                res.append(nums[i])
                maxi -= 1
                prev = nums[i]
                
        return res