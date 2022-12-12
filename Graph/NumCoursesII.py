class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        return self.hasCycle(numCourses, graph, indegree)

    def hasCycle(self, numCourses, graph, indegree):
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        order = []
        count = 0
        while queue:
            crs = queue.popleft()
            order.append(crs)
            count += 1
            for pre in graph[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)
        
        return order if count == numCourses else []