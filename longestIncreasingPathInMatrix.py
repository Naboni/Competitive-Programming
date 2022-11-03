class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        isvalid = lambda i, j: 0<=i<n and 0<=j<m
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for i in range(n):
            for j in range(m):
                indegree[(i, j)] = 0
                for x, y in direction:
                    nx, ny = i+x, j+y
                    if isvalid(nx, ny):
                        if matrix[i][j] > matrix[nx][ny]:
                            graph[(nx,ny)].add((i, j))
                            indegree[(i, j)] += 1
        
        q = deque([(key, 1) for key in indegree if indegree[key] == 0])
        res = 0
        while q:
            for _ in range(len(q)):
                node, dist = q.popleft()
                res = max(res, dist)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append((nei, dist+1))
        return res
        