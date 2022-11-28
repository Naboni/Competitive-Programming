n, m = map(int, input().split())

wghts = list(map(int, input().split()))
edges = []
for _ in range(m):
    x, y, w = list(map(int, input().split()))
    edges.append((w, x-1, y-1))

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

min_wght = min(wghts)
min_node = -1
for i in range(n):
    if wghts[i] == min_wght: 
        min_node = i

for i in range(n):
    if min_node != i:
        edges.append((wghts[i] + min_wght, min_node, i))

edges.sort()
uf = UnionFind()
res = 0
for w, x, y in edges:
    fx, fy = uf.find(x), uf.find(y)
    if fx != fy:
        uf.union(fx, fy)
        res += w

print(res)