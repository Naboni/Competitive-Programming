class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        center = len(nums) // 2
        left = nums[0:center]
        right = nums[center:len(nums)]
        pairs = []
        counter = len(left) - 1
        for i in range(len(left)):
            pairSum = left[i] + right[counter]
            pairs.append(pairSum)
            counter-=1
        return max(pairs)
