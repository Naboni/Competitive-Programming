from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.end = False

class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
        current.end = True

    def search(self, word):
        queue = [(self.root, 0)]
        while queue:
            node, index = queue.pop()
            if index == len(word):
                if node.end:
                    return True
                return False
            elif word[index] == ".":
                for nei in node.children.values():
                    queue.append((nei, index+1))
            elif word[index] in node.children:
                queue.append(node.children[word[index]], index+1)


    def dfs(self, node, word):
        if not word:
            if node.end:
                self.res = True
            return
        if word[0] == ".":
            for nei in node.children.values():
                self.dfs(nei, word[1:])
        else:
            if word[0] not in node.children:
                return
            self.dfs(node.children[word[0]], word[1:])