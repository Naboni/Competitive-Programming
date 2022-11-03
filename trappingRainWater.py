class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        curr = 0
        ans = 0
        while curr < len(height):
            while stack and height[stack[-1]] < height[curr]:
                h1 = stack.pop()
                if not stack: break
                h = min(height[curr], height[stack[-1]]) - height[h1]
                w = curr - stack[-1] -1
                ans += (h*w)
            stack.append(curr)
            curr += 1
        return ans