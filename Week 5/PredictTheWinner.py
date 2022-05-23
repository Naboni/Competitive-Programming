class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        def predict(nums):
            if len(nums) == 1:
                return nums[0]
            return max(nums[0]-predict(nums[1:]), 
                       nums[-1]-predict(nums[:-1]))
        score = predict(nums)
        return score >= 0
print(obj.PredictTheWinner([1,5,2]))
print(obj.PredictTheWinner([1,5,233,7]))
