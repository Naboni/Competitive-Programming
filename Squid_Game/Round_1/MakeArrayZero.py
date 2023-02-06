class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashset = set(nums)
        if 0 in hashset:
            return len(hashset)-1
        return len(hashset)