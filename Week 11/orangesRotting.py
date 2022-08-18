class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] 
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rw, cl = r+dr, c+dc
                    if rw in range(row) and cl in range(col) and grid[rw][cl] == 1:
                        grid[rw][cl] = 2
                        q.append((rw, cl))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
