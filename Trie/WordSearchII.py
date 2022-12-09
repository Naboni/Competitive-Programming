from collections import defaultdict

class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.refs = 0
        self.end = False

    def insert(self, word):
        current = self
        current.refs += 1
        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
            current.refs += 1
        current.end = True

    def remove(self, word):
        current = self
        current.refs -= 1
        for char in word:
            if char in current.children:
                current = current.children[char]
                current.refs -= 1

grid = []
n, m = map(int, input().split())
for _ in range(n):
    grid.append(list(map(str, input().split())))
words = list(map(str, input().split()))

trie = Trie()
for word in words:
    trie.insert(word)

result = set()
visited = set()

def dfs(r, c, node, word):
    if r<0 or c<0 or r==n or c==m or grid[r][c] not in node.children or node.children[grid[r][c]].refs < 1 or (r, c) in visited: return
    visited.add((r,c))
    node = node.children[grid[r][c]]
    word += grid[r][c]
    if node.end:
        node.end = False
        result.add(word)
        trie.remove(word)
    for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]: dfs(r+dr, c+dc, node, word)
    visited.remove((r, c))

for i in range(n):
    for j in range(m):
        dfs(i, j, trie, "")

print(list(result))