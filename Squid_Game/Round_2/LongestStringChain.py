class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordSet = set(words)
            
        cache = {}
        def dfs(word):
            if word in cache:
                return cache[word]
            path = 0
            for i in range(len(word)):
                newWord = word[:i] + word[i+1:]
                if newWord in wordSet:
                    path = max(path, dfs(newWord))
            
            cache[word] = path+1
            return cache[word]
        
        maxPath = 1
        for word in words:
            maxPath = max(maxPath, dfs(word))
        return maxPath