from collections import defaultdict
import heapq

class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for i in word:
            cur = cur.children[i]
        cur.end = True
    
    def autocomplete(self, char):
        cur = self.root
        for i in char:
            cur = cur.children[i]
        res = []
        def btrc(cur, path):
            if cur.end:
                res.append("".join(path[::-1]))
                return
            for key in cur.children:
                btrc(cur.children[key], [key] + path)
        btrc(cur, [])
        
        return [char+i for i in res]

class AutoCompleteSearch:
    def __init__(self, sentences) -> None:
        self.sentences = defaultdict(int)
        self.trie = Trie()
        for key in sentences:
            self.trie.add(key)
            self.sentences[key] = sentences[key]

    def search(self, chars):
        ans = self.trie.autocomplete(chars)
        self.sentences[chars] += 1
        res = []
        for el in ans:
            res.append((self.sentences[el], el))
        return [y for x, y in sorted(res, reverse=True)[:3]]

obj = AutoCompleteSearch({"i love you":5, "island": 3, "ironman": 2, "i love leetcode": 2, "babyies": 5})
print(obj.search("i"))