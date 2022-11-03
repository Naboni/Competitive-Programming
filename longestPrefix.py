class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        left, right = 0, 1
        while right < len(s):
            if s[left] == s[right]:
                lps[right] = left + 1
                left += 1
                right += 1
            else:
                if left == 0:
                    lps[right] = 0
                    right += 1
                else:
                    left = lps[left - 1]
        return s[0:lps[-1]]