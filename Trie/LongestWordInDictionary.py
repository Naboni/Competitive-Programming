# 720. Longest Word in Dictionary

from collections import defaultdict, deque

n = int(input())
words = []
for _ in range(n):
    words.append(input())

class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.end = False
        self.word = ""

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
        current.end = True
        current.word = word

    def bfs(self):
        queue = deque([self.root])
        res = ""
        while queue:
            node = queue.popleft()
            for nei in node.children.values():
                if nei.end:
                    queue.append(nei)
                    ans = nei.word
                    if len(ans) > len(res) or ans < res:
                        res = ans
        return res
        
trie = Trie()
for word in words:
    trie.insert(word)

print(trie.bfs())