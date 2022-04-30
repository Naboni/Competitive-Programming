class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        allPairs = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] == nums[j]:
                    newPair = [i,j]
                    newPair.sort()
                    if not newPair in allPairs:
                        allPairs.append(newPair)
        return len(allPairs)
