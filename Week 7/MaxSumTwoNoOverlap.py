class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        maxFirst = maxSec = summ = 0
        for x in nums:
            prefix.append(prefix[-1] + x)
        
        for x in range(secondLen, len(prefix) - firstLen):
            maxSec = max(maxSec, prefix[x] - prefix[x - secondLen])
            summ = max(summ, maxSec + prefix[x + firstLen] - prefix[x])
        
        for x in range(firstLen, len(prefix) - secondLen):
            maxFirst = max(maxFirst, prefix[x] - prefix[x - firstLen])
            summ = max(summ, maxFirst + prefix[x + secondLen] - prefix[x])
        
        return summ
