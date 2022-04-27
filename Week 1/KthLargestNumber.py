class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        intNum = [int(num) for num in nums]
        intNum.sort()
        return(str(intNum[len(nums)-k]))
