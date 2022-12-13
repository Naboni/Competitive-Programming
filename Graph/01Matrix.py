class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        visited = set()
        queue = deque()
        ans = [[0 for _ in range(m)] for _ in range(n)]
        distance = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i,j))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if mat[r][c] == 1:
                    ans[r][c] = distance
                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<n and 0<=nc<m and (nr,nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            distance += 1
        
        return ans