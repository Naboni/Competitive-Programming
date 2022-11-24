class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy: return False
        if self.rank[fx] >= self.rank[fy]:
            self.parent[fy] = fx
            self.rank[fx] += self.rank[fy]
        else:
            self.parent[fx] = fy
            self.rank[fy] += self.rank[fx]

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1

        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]