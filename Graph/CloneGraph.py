"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        nodeMap = {}
        queue = deque([node])
        visited = set()
        while queue:
            n = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n not in nodeMap:
                nodeMap[n] = Node(n.val)
            for nei in n.neighbors:
                if nei not in nodeMap:
                    nodeMap[nei] = Node(nei.val)
                nodeMap[n].neighbors.append(nodeMap[nei])
                if nei not in visited:
                    queue.append(nei)
        return nodeMap[node]