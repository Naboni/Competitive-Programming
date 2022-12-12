class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificVisited, atlanticVisited = set(), set()
        n, m = len(heights), len(heights[0])
        
        for i in range(n):
            self.dfs(i, 0, n, m, pacificVisited, heights)
            self.dfs(i, m-1, n, m, atlanticVisited, heights)

        for j in range(m):
            self.dfs(0, j, n, m, pacificVisited, heights)
            self.dfs(n-1, j, n, m, atlanticVisited, heights)

        return pacificVisited.intersection(atlanticVisited)

    def dfs(self, r, c, n, m, visited, heights):
        visited.add((r, c))
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0<=nr<n and 0<=nc<m and heights[r][c] <= heights[nr][nc] and (nr, nc) not in visited:
                visited.add((nr, nc))
                self.dfs(nr, nc, n, m, visited, heights)