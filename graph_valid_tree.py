from collections import deque


n = int(input())
x = int(input())
edges = []
for _ in range(x):
    edges.append(map(int, input().split()))

def solve():
    graph = {i:[] for i in range(n)}
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
        if len(graph[x]) > 3 or len(graph[y]) > 3: return False
    # print(graph)
    # detect cycle in undirected graph
    visited = set()
    nodesCount = [0]
    def hasCycle(node, par):
        nodesCount[0] += 1
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if hasCycle(nei, node):
                    return True
            elif nei != par:
                return True
        return False
    return not hasCycle(0, -1) and n == nodesCount[0]
    
if solve():
    print("Yes")
else:
    print("No")