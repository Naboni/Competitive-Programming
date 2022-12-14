class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy: return
        if self.rank[fy] > self.rank[fx]:
            fx, fy = fy, fx
        
        self.parent[fy] = fx
        self.rank[fx] = fy

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        for x, y in edges:
            fx = uf.find(x)
            fy = uf.find(y)
            if fx == fy: return [x, y]
            uf.union(x, y)
        return res