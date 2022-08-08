class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        
        def dfs(i):
            for x, val in enumerate(isConnected[i]):
                if val == 1 and x not in visited:
                    visited.add(x)
                    dfs(x)
                    
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
