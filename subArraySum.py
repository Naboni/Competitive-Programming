class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        res = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            kDiff = prefix - k
            res += count.get(kDiff, 0)
            count[prefix] = count.get(prefix, 0) + 1
        return res