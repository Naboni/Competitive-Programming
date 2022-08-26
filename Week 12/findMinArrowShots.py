class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count = 1
        arr = points[0][1]
        for s, e in points[1:]:
            if arr >= s:
                continue
            else:
                arr = e
                count += 1
        return count
