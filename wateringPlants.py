class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        bucket = capacity
        steps = 0
        i = 0
        while i < len(plants):
            if bucket - plants[i] >= 0:
                steps += 1
                bucket -= plants[i]
                i += 1
            else:
                bucket = capacity
                steps += (2*i + 1)
                bucket -= plants[i]
                i += 1
        return steps