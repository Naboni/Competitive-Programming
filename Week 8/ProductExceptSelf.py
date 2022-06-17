class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        
        prefix = 1
        for i in range(length-1):
            prefix = prefix * nums[i]
            res[i+1] = prefix
        
        postfix = 1
        for i in range(length-1,-1,-1):
            res[i] *= postfix
            postfix = postfix * nums[i]
            
        return res
