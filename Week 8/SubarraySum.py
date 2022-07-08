class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        output = 0
        count = {0:1}
        for num in nums:
            currSum += num
            kDiff = currSum - k
            output += count.get(kDiff, 0)
            count[currSum] = count.get(currSum, 0) + 1
        return output
