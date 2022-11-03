class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        
        q = deque([0])
        visited = set([0])
        directions = [x, -x, y, -y]
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == z:
                    return True
                for i in directions:
                    new = curr + i
                    if 0 < new <= x+y and new not in visited:
                        q.append(new)
                        visited.add(new)
        return False