class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y, s in roads:
            graph[x].append((y, s))
            graph[y].append((x, s))
        
        q = [(inf, 1)]
        res = inf
        visited = set([1])
        while q:
            d, n = q.pop()
            for x, s in graph[n]:
                if x not in visited:
                    visited.add(x)
                    q.append((min(s,d), x))
                res = min(res, min(s,d))
        return res