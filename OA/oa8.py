from collections import Counter, defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.isWord = False
        self.freq = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
            curr.freq += 1
        curr.isWord = True

    def find(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        return curr.freq

obj = Trie()
words = ["back", "backgammon", "backdoor", "gammon", "come", "comeback", "door"]
# words = ["abc", "a", "a", "b", "ab", "ac"]
for word in words:
    obj.insert(word)

wordsMap = Counter(words)
result = 0
for key in wordsMap:
    find = obj.find(key)
    x = wordsMap[key] * (find - wordsMap[key])
    y = (wordsMap[key] * (wordsMap[key] - 1)) // 2
    result += x + y

print(result)