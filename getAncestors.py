class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [set() for _ in range(n)]
        graph = defaultdict(list)
        incoming = [0]*n
        for x, y in edges:
            graph[x].append(y)
            incoming[y] += 1
        q = deque()
        for ind, val in enumerate(incoming):
            if val == 0:
                q.append(ind)
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                incoming[neigh] -= 1
                res[neigh].add(node)
                for ind, val in enumerate(res[node]):
                    res[neigh].add(val)
                if incoming[neigh] == 0:
                    q.append(neigh)
        return map(lambda x: sorted(x), res)