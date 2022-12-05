from functools import lru_cache


def maxPalindromes(s, k):
    @lru_cache(None)
    def dp(left):
        if left > len(s) - k:
            return 0
        res = 0
        size = left + k
        for right in range(size, size+2):
            word = s[left:right]
            if word == word[::-1]:
                res = max(res, 1 + dp(right))
        return max(res, dp(left+1))
    return dp(0)
s = input()
k = int(input())
print(maxPalindromes(s, k))