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
        graph = defaultdict(list)
        importanceMap = {}
        for i in range(len(employees)):
            importanceMap[employees[i].id] = employees[i].importance
            for nei in employees[i].subordinates:
                graph[employees[i].id].append(nei)
        
        queue = deque([id])
        visited = set([id])
        res = 0
        while queue:
            node = queue.popleft()
            res += importanceMap[node]
            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)
        
        return res