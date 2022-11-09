class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sett = set()
        size = len(nums)
        ans = []
        for i in nums:
            if i in sett:
                ans.append(i)
            sett.add(i)
        for i in range(1, size+1):
            if i not in sett:
                ans.append(i)
                break
        return ans