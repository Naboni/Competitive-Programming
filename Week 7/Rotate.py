class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1 Time O(n) Space O(n)
        n = len(nums)
        a = [0]*n
        for i in range(n):
            a[(i+k)%n] = nums[i]
        for i in range(n):
            nums[i] = a[i]
        
        # Approach 2 Time O(n) Space O(n)
        # n = len(nums)
        # l, r = 0, n-1 
        # k %= n
        # while l<r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l, r = l+1, r-1
        # l, r = 0, k-1
        # while l<r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l, r = l+1, r-1
        # l, r = k, n-1
        # while l<r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l, r = l+1, r-1
