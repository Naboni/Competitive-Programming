class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time and O(n) memory
        # n = len(nums)
        # prefix = [1]*n
        # suffix = [nums[-1]]*n
        # output = [0]*n
        # for i in range(n):
        #     if i == 0:
        #         prefix[i] = nums[i]
        #     else:
        #         prefix[i] = prefix[i-1] * nums[i]
        # for i in range(n-1, -1, -1):
        #     if i == (n-1):
        #         suffix[i] = nums[i]
        #     else:
        #         suffix[i] = suffix[i+1] * nums[i]
        # for i in range(n):
        #     if i == 0:
        #         output[i] = suffix[i+1]
        #     elif i == (n-1):
        #         output[i] = prefix[i-1]
        #     else:
        #         output[i] = prefix[i-1] * suffix[i+1]
        # return output
        # O(n) time and O(1) memory
        n = len(nums)
        output = [1]*n
        pre = 1
        for i in range(1,n):
            pre *= nums[i-1]
            output[i] = pre
        post = 1
        for i in range(n-2, -1, -1):
            post *= nums[i+1]
            output[i] *= post
        return output
        
