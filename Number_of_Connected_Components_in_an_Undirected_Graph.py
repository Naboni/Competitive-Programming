from UnionFind import UnionFind

n = int(input())
x = int(input())

edges = []
for _ in range(x):
    edges.append(map(int, input().split()))

uf = UnionFind()

for x, y in edges:
    uf.union(x, y)

pars = set()
for i in range(n):
    pars.add(uf.find(i))

print(len(pars))