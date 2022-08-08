class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val = image[sr][sc]
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r == len(image) or c == len(image[0]) or image[r][c] != val or (r, c) in visited:
                return
            image[r][c] = color
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions:
                dfs(dr+r, dc+c)
        dfs(sr, sc)
        return image
