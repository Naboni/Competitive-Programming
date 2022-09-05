class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(cost):
                return 0
            if i == len(cost)-1:
                cache[i] = cost[i]
                return cost[i]
            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]
        dfs(0)
        return min(cache[0], cache[1])
    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])
