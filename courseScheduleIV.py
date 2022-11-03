class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            pre[c1][c2] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    pre[i][j] = pre[i][j] or (pre[i][k] and pre[k][j])
        res = [False] * len(queries)
        for i, (x, y) in enumerate(queries):
            res[i] = pre[x][y]
        return res