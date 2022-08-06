class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def sumByDivisor(num):
            total = 0
            for n in nums:
                total += ceil(n/num)
            return total
        
        l, r = 1, max(nums)
        while l <= r:
            m = (l+r)//2
            summ = sumByDivisor(m)
            if summ > threshold:
                l = m + 1
            else:
                r = m - 1
        return l
