class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        q=deque([(dp[0],0)])
        for i in range(1,n):
            dp[i]=q[0][0]+nums[i]
            while q and dp[i]>q[-1][0]:
                q.pop()
            q.append((dp[i],i))
            if q[0][1]<=i-k:
                q.popleft()
        return dp[n-1]
