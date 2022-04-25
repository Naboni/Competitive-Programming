class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if(len(intervals) <= 1):
            return intervals
        intervals.sort()
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = merged[-1][1] if merged[-1][1] > interval[1] else interval[1]
        
        return merged
