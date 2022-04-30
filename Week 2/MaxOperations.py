from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pair = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            j = k - nums[i]
            if(pair[j] == 0):
                pair[nums[i]] += 1
            else:    
                count +=1
                pair[j] -= 1
        return count
