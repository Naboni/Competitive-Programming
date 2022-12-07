class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.freq = 0
        self.end = False
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root
        for char in word:
            index = ord(char) - ord("a")
            if current.children[index] == None:
                current.children[index] = TrieNode()
            current = current.children[index]
            current.freq += 1
        current.end = True
    
    def search(self, prefix):
        current = self.root
        for char in prefix:
            index = ord(char) - ord("a")
            if current.children[index] == None:
                return False
            current = current.children[index]
        return current.end

    def find(self, word):
        current = self.root
        for char in word:
            index = ord(char) - ord("a")
            if current.children[index] == None:
                return 0
            current = current.children[index]
        return current.freq

words = list(map(str, input().split()))
obj = Trie()
for word in words:
    obj.addWord(word)

for query in words:
    print(obj.find(query))
