class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = [0]*4 #0, 1, 01, 10
        res = 0
        for i in s:
            if i == "0": 
                dp[0] += 1
                dp[3] += dp[1]
                res += dp[2]
            else:
                dp[1] += 1
                dp[2] += dp[0]
                res += dp[3]
        return res