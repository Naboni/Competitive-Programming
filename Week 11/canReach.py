class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = set()
        while q:
            ind = q.popleft()
            if arr[ind]==0:
                return True
            visited.add(ind)
            x, y = ind + arr[ind], ind - arr[ind]
            if x in range(len(arr)) and x not in visited:
                q.append(x)
            if y in range(len(arr)) and y not in visited:
                q.append(y)
        return False
