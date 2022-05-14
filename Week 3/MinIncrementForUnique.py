class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        output=0
        for i in range(1, len(nums)):
            if nums[i]<=nums[i-1]:
                diff=(nums[i-1]-nums[i])+1
                nums[i]=nums[i]+diff
                output+=diff
        return output
