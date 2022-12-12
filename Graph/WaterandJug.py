class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        queue = deque([0])
        visited = set([0])
        options = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]

        while queue:
            curr = queue.popleft()
            if curr == targetCapacity: return True
            for option in options:
                new = curr + option
                if 0 < new <= jug1Capacity + jug2Capacity and new not in visited:
                    queue.append(new)
                    visited.add(new)
        return False 