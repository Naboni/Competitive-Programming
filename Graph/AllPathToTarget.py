class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.helper(0, [0], graph)
        return self.res
        
    def helper(self, node, path, graph):
        if node == len(graph)-1:
            self.res.append(path)
            return
        for nei in graph[node]:
            self.helper(nei, path+[nei], graph)