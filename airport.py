class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.rank = {}

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy: return
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

        if x != self.parent[x]:
            return self.find(self.parent[x])
        return x

ports = list(map(str, input().split()))
n = int(input())
routes = []
for _ in range(n):
    routes.append(list(map(str, input().split())))

print(routes)