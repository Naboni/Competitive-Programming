class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row+1)]
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    dp[i+1][j] = dp[i][j] + int(matrix[i][j])
        res = 0
        for row in dp[1:]:
            res = max(res, self.maxHistogramArea(row))
        return res
            
    def maxHistogramArea(self, arr: List[int]) -> int:
        n = len(arr)
        left, stack = [0]*n, []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)
        stack = []
        res = 0
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right = n-1 if not stack else stack[-1] - 1
            stack.append(i)
            res = max(res, arr[i] * (right-left[i]+1))
        return res
