class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = [str(i) for i in digits]
        s = "".join(dig)
        num = int(s) + 1
        return [i for i in str(num)]