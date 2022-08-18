class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(0,0,0)]
        visited = set()
        res = grid[0][0]
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        while heap:
            currTime, row, col = heapq.heappop(heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            res = max(res, currTime)
            if (row, col) == (n-1, n-1):
                return res
            for dr, dc in directions:
                x, y = row + dr, col + dc
                if 0 <= x < n and 0 <= y < n:
                    heapq.heappush(heap, (grid[x][y], x, y))
        return res
