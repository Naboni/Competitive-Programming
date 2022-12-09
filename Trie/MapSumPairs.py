from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.value = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word, val):
        current = self.root
        for char in word:
            current = current.children[char]
            current.value += val
    
    def sum(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.value

class MapSum:
    def __init__(self) -> None:
        self.trie = Trie()
        self.hashmap = {}

    def insert(self, key, val):
        if key not in self.hashmap:
            self.hashmap[key] = val
            self.trie.insert(key, val)
        else:
            upd = val - self.hashmap[key]
            self.hashmap[key] = val
            self.trie.insert(key, upd)
    
    def sum(self, prefix):
        return self.trie.sum(prefix)