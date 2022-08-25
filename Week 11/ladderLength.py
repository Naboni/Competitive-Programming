class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList) # for lookup optimization O(1)
        if endWord not in words: 
            return 0
        graph = defaultdict(set)
        
        for word in wordList:
            for ind, letter in enumerate(word):
                graph[ind].add(letter)
        
        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        while q:
            word, distance = q.popleft()
            if word == endWord:
                return distance
            for i in range(len(word)):
                for letter in graph[i]:
                    newWord = word[:i] + letter + word[i+1:]
                    if newWord in words and newWord not in visited:
                        visited.add(newWord)
                        q.append((newWord, distance+1))
        return 0
