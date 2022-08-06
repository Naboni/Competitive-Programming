class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def shipDays(capacity):
            day = 1
            cap = 0
            for n in weights:
                cap += n
                if cap > capacity:
                    day += 1
                    cap = n
            return day
        
        l, r = max(weights), sum(weights)
        while l<=r:
            m = (l+r)//2
            if shipDays(m) <= days:
                r = m-1
            else:
                l = m+1
        return l
