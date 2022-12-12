class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append((i, 1))
        
        result = [0] * n
        while queue:
            node, dist = queue.popleft()
            result[node] = max(result[node], dist)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append((nei, dist+1))
        maxi = max(result)
        return [node for node in range(n) if result[node] == maxi]