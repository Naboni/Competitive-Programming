class Solution:
    def __init__(self):
        self.k = 31
        self.MOD = 10**9 + 7

    def strStr(self, haystack: str, needle: str) -> int:
        needle_hash = self.wordhash(needle)
        hashed = 0
        left = 0
        for i in range(len(haystack)-len(needle)+1):
            if i-left+1 <= len(needle):
                hashed += ((ord(haystack[i])-ord("a")+1) * (self.k ** (i-left))) % self.MOD
            else:
                if hashed == needle_hash:
                    return left
                else:
                    hashed -= ord(haystack[left])
                    hashed //= self.k
                    left += 1
        return -1

    def wordhash(self, word: str) -> int:
        word_hash = 0
        for i in range(len(word)):
            char_hash = ((ord(word[i]) - ord("a") + 1) * (self.k ** i)) % self.MOD
            word_hash += char_hash
        return word_hash