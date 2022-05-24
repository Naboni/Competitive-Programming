class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        score = self.play(nums)
        return score >= 0
    
    def play(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(nums[0] - self.play(nums[1:]), nums[-1] - self.play(nums[:-1]))

print(obj.PredictTheWinner([1,5,2]))
print(obj.PredictTheWinner([1,5,233,7]))
