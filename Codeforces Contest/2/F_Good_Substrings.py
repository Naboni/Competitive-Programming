from collections import defaultdict
 
 
s = input()
bads = list(map(int, input()))
k = int(input())
 
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False
 
root = Node()
ans = 0
for i in range(len(s)):
    node = root
    bad_count = 0
 
    for j in range(i, len(s)):
        bad_count += 1- bads[ord(s[j]) - ord('a')]
 
        if bad_count > k:
            break
        
        node  = node.children[s[j]]
        if not node.end:
            ans += 1
        
        node.end = True
 
print(ans)