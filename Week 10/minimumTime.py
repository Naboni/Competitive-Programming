class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, max(time)*totalTrips
        res = 0
        while l<=r:
            m = (l+r)//2
            count = 0
            for t in time:
                count += m//t
            if count >= totalTrips:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
