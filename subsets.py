class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()
        self.subsets([], nums)
        return self.result

    def subsets(self, path, nums):
        self.result.append(path)
        for i in range(len(nums)):
            if i==0 or nums[i] != nums[i-1]:
                self.subsets(path+[nums[i]], nums[i+1:])