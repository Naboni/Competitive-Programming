from ast import List
from collections import defaultdict

class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.words = set()

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, index, word):
        current = self.root
        for char in word:
            current = current.children[char]
            current.words.add(index)
    
    def startsWith(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
            if current.words is None:
                return set()
        return current.words

class WordFilter:
    def __init__(self, words: List[str]):
        self.forwardTrie, self.backwardsTrie = Trie(), Trie()
        filteredWords, self.searchResults = {}, {}
        
        for i, word in enumerate(words):
            filteredWords[word] = i
        
        for word, i in filteredWords.items():
            self.forwardTrie.insert(i, word)
            self.backwardsTrie.insert(i, reversed(word))

    def f(self, prefix: str, suffix: str) -> int:
        if prefix + "-" + suffix not in self.searchResults.keys():
            prefixSearch = self.forwardTrie.startsWith(prefix)
            suffixSearch = self.backwardsTrie.startsWith(reversed(suffix))
            searchResults = prefixSearch.intersection(suffixSearch)
            self.searchResults[prefix + "-" + suffix] = max(searchResults) if searchResults else -1
            
        return self.searchResults[prefix + "-" + suffix]