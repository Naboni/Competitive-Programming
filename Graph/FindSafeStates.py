class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        safe = {}
        for node in range(len(graph)):
            if self.isSafe(node, graph, safe):
                result.append(node)
        return result

    def isSafe(self, node, graph, safe):
        if node in safe: return safe[node]
        safe[node] = False
        for nei in graph[node]:
            if not self.isSafe(nei, graph, safe):
                return False
        safe[node] = True
        return True