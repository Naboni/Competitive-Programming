"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashmap = {emp.id: emp for emp in employees}
        # Iterative DFS
        # stack = [hashmap[id]]
        # res = 0
        # while stack:
        #     emp = stack.pop()
        #     res += emp.importance
        #     for sub in emp.subordinates:
        #         stack.append(hashmap[sub])
        # return res
        
        # Recursive DFS
        res = [0]
        def dfs(idd):
            res[0] += hashmap[idd].importance
            for sub in hashmap[idd].subordinates:
                dfs(sub)
            return res[0]
        return dfs(id)
