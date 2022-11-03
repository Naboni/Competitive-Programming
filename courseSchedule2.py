class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        res = []
        incoming = [0]*numCourses
        for x, y in prerequisites:
            graph[x].append(y)
            incoming[y] += 1
        q = deque([])
        for ind, val in enumerate(incoming):
            if val == 0:
                q.append(ind)
        while q:
            node = q.popleft()
            res.append(node)
            for neigh in graph[node]:
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    q.append(neigh)
        if len(res) == numCourses:
            return res[::-1]
        return []