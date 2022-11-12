def dfs(adjList):
    res = []
    def ds(root, parent):
        res.append(root)
        for i in range(len(adjList[root])):
            node = adjList[root][i]
            if node != parent:
                ds(node, root)
    ds(0, -1)
    return res

print(dfs([[1, 3, 6], [0, 2, 4], [1], [0], [1, 5], [4], [0]]))