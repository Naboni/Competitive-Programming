class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for x, y in prerequisites:
            graph[x].append(y)
            indegree[y] += 1
        return self.hasCycle(numCourses, graph, indegree)

    def hasCycle(self, numCourses, graph, indegree):
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        crsTaken = 0
        while queue:
            crs = queue.popleft()
            crsTaken += 1
            for pre in graph[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)
        return crsTaken == numCourses