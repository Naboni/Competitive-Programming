class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = ([0] * len(nums))[:len(nums)]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    arr[i]+=1
        return arr
