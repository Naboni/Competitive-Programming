class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    result += 1
                    self.dfs(i, j, n, m, grid)
        return result

    def dfs(self, r, c, n, m, grid):
        if r<0 or c<0 or r==n or c==m or grid[r][c] != "1": return
        grid[r][c] = "0"
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            self.dfs(r+dr, c+dc, n, m, grid)