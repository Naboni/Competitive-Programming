class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        for i in range(n):
            if colors[i] == -1 and not self.dfs(i, 0, colors, graph):
                return False
        return True    

    def dfs(self, node, color, colors, graph):
        colors[node] = color
        for nei in graph[node]:
            if colors[nei] == color: return False
            if colors[nei] == -1 and not self.dfs(nei, 1-color, colors, graph): return False
        return True