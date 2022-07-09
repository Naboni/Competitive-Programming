class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prevSum = 0
        output = 0
        for n in nums:
            prevSum += 0 if n % 2 == 0 else 1
            kdiff = prevSum - k
            output += count.get(kdiff, 0)
            count[prevSum] = count.get(prevSum, 0) + 1
        return output
