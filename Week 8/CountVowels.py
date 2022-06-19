class Solution:
    def countVowels(self, word: str) -> int:
        vowels = "aeiou"
        length, output = len(word), 0
        for i, vowel in enumerate(word):
            if vowel in vowels:
                output += (length - i) * (i + 1)
        return output
