class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return

        step = len(nums) - k
        left = 0
        while left != len(nums) - 1 and k:
            right = left + step
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            if left + step > len(nums) - 1:
                new_size = (right - left) + 1
                k %= new_size
                step -= k
