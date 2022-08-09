class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r<0 or c<0 or r==m or c==n or grid[r][c] != 1:
                return
            grid[r][c] = -1
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and r in [0,m-1] or c in [0,n-1]:
                    dfs(r,c)
                    
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    count += 1
        return count
