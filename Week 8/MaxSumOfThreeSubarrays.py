class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        m = 3
        dp = [[0]*(m+1) for _ in range(n+1)]
        index = [[0]*(m+1) for _ in range(n+1)]
        
        presum = [0]
        total = 0
        for num in nums:
            total += num
            presum.append(total)

        for j in range(1,m+1):
            for i in range(k*j, len(nums)+1):
                max_prev_sum = dp[i-k][j-1] + presum[i] - presum[i-k]
                
                if dp[i-1][j] < max_prev_sum:
                    dp[i][j] = max_prev_sum
                    index[i][j] = i-k
                else:
                    dp[i][j] = dp[i-1][j]
                    index[i][j] = index[i-1][j]
                    
        output = []
        i, sn = n, m
        for _ in range(m):
            output.append(index[i][sn])
            i = index[i][sn]
            sn -= 1
        return output[::-1]
