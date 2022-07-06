class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder = []
        for i in range(len(heights)-1):
            climbed = heights[i+1] - heights[i]
            if climbed <= 0:
                continue
            if ladders > 0:
                heappush(ladder, climbed)
                ladders -= 1
            else: 
                if ladder and ladder[0] < climbed:
                    bricks -= heappop(ladder)
                    heappush(ladder, climbed)
                else:
                    bricks -= climbed
                if bricks < 0:
                    return i
        return len(heights) - 1
