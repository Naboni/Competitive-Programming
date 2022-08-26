class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        
        for i in range(len(nums) - 1): 
            maxi = max(nums[-1] - k, nums[i] + k)
            mini = min(nums[0] + k, nums[i + 1] - k)
            res = min(res, maxi - mini)
        
        return res
