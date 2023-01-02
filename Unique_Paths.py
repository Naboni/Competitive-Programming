class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        start_r, start_c, end_r, end_c = 0, 0, 0, 0
        empty = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    start_r, start_c = i, j
                elif grid[i][j] == 2:
                    end_r, end_c = i, j
                elif grid[i][j] == 0:
                    empty += 1
        
        visited = set()
        self.res = 0
        def dfs(r, c, visited, walk):
            if r == end_r and c == end_c:
                if walk == empty+1:
                    self.res += 1
                return  #lol u failed here right
            if 0<=r<row and 0<=c<col and grid[r][c] != -1 and (r, c) not in visited:
                visited.add((r, c))
                for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    dfs(r+i, c+j, visited, walk+1)
                visited.remove((r, c))
        
        dfs(start_r, start_c, visited, 0)
        return self.res