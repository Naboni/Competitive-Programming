class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, maxi = 0, 0, 0
        while r<len(nums):
            if nums[r] == 0:
                if k > 0:
                    k -= 1
                else:
                    maxi = max(maxi, r-l)
                    if nums[l] == 0:
                        k+=1
                    l += 1
                    continue
            r+=1
        return max(maxi, r-l)