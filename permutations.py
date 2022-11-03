class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.permutations(nums, [], len(nums))
        return self.result
    
    def permutations(self, nums, path, length):
        if len(path) == length:
            self.result.append(path)
            return
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            self.permutations(new_nums, path+[nums[i]], length)