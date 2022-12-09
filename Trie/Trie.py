from collections import defaultdict

class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
        current.end = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end
    
    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True