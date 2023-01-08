class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def dp(a, clip):
            if a > n: return inf
            if a == n: return 0
            copy = paste = inf
            if a != clip:
                copy = dp(a, a)
            if clip != 0:
                paste = dp(a+clip, clip)
            return 1 + min(copy, paste)
        return dp(1, 0)