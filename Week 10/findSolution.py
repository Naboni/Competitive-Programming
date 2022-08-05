"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        l, r = 1, z
        pairs = []
        while l <= z and r > 0:
            res = customfunction.f(l,r)
            if res == z:
                pairs.append([l,r])
                l, r = l+1, r-1
            elif res > z:
                r -= 1
            else:
                l += 1
        return pairs
