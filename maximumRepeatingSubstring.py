class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        left, right = 0, len(word)
        res = count = 0

        while right <= len(sequence):
            if sequence[left:right] == word:
                count += 1
                left = right
                right += len(word)
                while True:
                    if sequence[left:right] != word:
                        left -= len(word) - 1
                        right = left + len(word)
                        res = max(res, count)
                        count = 0
                        break
                    count += 1
                    left = right
                    right += len(word)
            else:
                left += 1
                right += 1
        return res