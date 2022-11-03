class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        left, stack = [0] * n, []  
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)
        res = 0
        right, stack = [0] * n, []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = n-1 if not stack else stack[-1] - 1
            stack.append(i)
            res = max(res, (right[i] - left[i] + 1) * heights[i])
        