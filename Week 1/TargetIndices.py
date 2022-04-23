class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i-1
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
                    
        for i in range(n):
            if nums[i] == target:
                output.append(i)
        return output
