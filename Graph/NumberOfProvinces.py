class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = set()
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        for i in range(len(isConnected)):
            if i not in visited:
                self.dfs(i, visited, graph)
                count += 1
        return count

    def dfs(self, node, visited, graph):
        if node in visited: return
        visited.add(node)
        for nei in graph[node]:
            self.dfs(nei, visited, graph)