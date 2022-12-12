class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx, (x, y) in enumerate(equations):
            graph[x].append((y, values[idx]))
            graph[y].append((x, 1/values[idx]))

        result = []
        for x, y in queries:
            if x in graph and y in graph:
                result.append(self.bfs(x, y, graph))
            else:
                result.append(-1.0)
        return result

    def bfs(self, x, y, graph):
        queue = deque([(x,1)])
        visited = set([(x,1)])

        while queue:
            var, const = queue.popleft()
            if var == y:
                return const
            for nei, k in graph[var]:
                new = const * k
                if (nei, new) not in visited:
                    queue.append((nei, new))
                    visited.add((nei, new))
        return -1.0