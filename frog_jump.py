class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        res = stones[1] - stones[0]
        for i in range(n-2):
            res = max(res, stones[i+2] - stones[i])
        return res