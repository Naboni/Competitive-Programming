class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        # island = 0
        row, col = len(grid), len(grid[0])
        visited = set()
        maxGraphSize = [0]
        
        # iterative
        def dfs(r, c, maxGraphSize):
            q = []
            visited.add((r, c))
            q.append((r, c))
            count = 1
            while q:
                r, c = q.pop()
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    rw, cl = r + dr, c + dc
                    if rw in range(row) and cl in range(col) and grid[rw][cl] == 1 and (rw, cl) not in visited:
                        visited.add((rw, cl))
                        q.append((rw, cl))
                        ila+=1
            maxGraphSize[0] = max(maxGraphSize[0], count)
        
        # recursive
        def dfsr(r, c):
            if r < 0 or c < 0 or r == row or c == col or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return 1 + dfsr(r+1, c) + dfsr(r-1, c) + dfsr(r, c+1) + dfsr(r, c-1)
        
        area = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    # dfs(r, c, maxGraphSize)
                    area = max(area, dfsr(r, c))
                    # island += 1
        # return maxGraphSize[0]
        return area
