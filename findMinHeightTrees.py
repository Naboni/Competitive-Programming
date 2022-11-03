class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        q = deque()
        for i in indegree:
            if indegree[i] == 1:
                q.append((i, 1))
        res = [0]*n
        while q:
            node, dist = q.popleft()
            res[node] = max(res[node], dist)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append((nei, dist+1))
        maxi = max(res)
        print(res)
        return [i for i, val in enumerate(res) if val == maxi]
