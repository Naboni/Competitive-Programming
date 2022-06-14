class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end, maxi, n = 0, 0, 0, len(nums)
        while end < n:
            if nums[end] == 0:
                if k > 0:
                    k -= 1
                else:                  
                    maxi = max(maxi, end - start)
                    if nums[start] == 0:
                        k += 1
                    start += 1
                    continue
            end += 1 
        return max(maxi, end - start)
