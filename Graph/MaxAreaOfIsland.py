class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        n, m = len(grid), len(grid[0])
        result = 0
        for i in range(n):
            for j in range(m):
                result = max(result, self.dfs(i, j, n, m, grid, visited))
        return result
        
    def dfs(self, r, c, n, m, grid, visited):
        if r<0 or c<0 or r==n or c==m or (r,c) in visited or grid[r][c] == 0: return 0
        visited.add((r, c))
        res = 1
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            res += self.dfs(r+dr, c+dc, n, m, grid, visited)
        return res