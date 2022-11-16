class Solution:
    def gameOfLife(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]
        for i in range(n):
            for j in range(m):
                ones = 0
                for x, y in directions:
                    nx, ny = i+x, j+y
                    if 0<=nx<n and 0<=ny<m:
                        if grid[nx][ny] == 1 or grid[nx][ny] == -2:
                            ones += 1
                if grid[i][j] == 1 and (ones < 2 or ones > 3):
                    grid[i][j] = -2
                elif grid[i][j] == 0 and ones == 3:
                    grid[i][j] = 2
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -2:
                    grid[i][j] = 0
                elif grid[i][j] == 2:
                    grid[i][j] = 1