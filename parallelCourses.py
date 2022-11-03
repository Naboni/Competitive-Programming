class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        inorder = [0]*n
        for x, y in relations:
            x, y = x-1, y-1
            graph[x].append(y)
            inorder[y] += 1
        duration = [0]*n
        q = deque()
        for i in range(n):
            if inorder[i] == 0:
                q.append(i)
                duration[i] = time[i]
        while q:
            t = q.popleft()
            for nei in graph[t]:
                duration[nei] = max(duration[nei], time[nei] + duration[t])
                inorder[nei] -= 1
                if inorder[nei] == 0:
                    q.append(nei)
        return max(duration)