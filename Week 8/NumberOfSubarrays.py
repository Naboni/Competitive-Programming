class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prevCount = defaultdict(int)
        prevCount[0] = 1
        output = 0
        count = 0
        for num in nums:
            if num % 2 == 1:
                count += 1
            prevCount[count] += 1
            if count - k in prevCount:
                output += prevCount[count - k]
        return output