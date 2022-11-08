class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        first = sec = 0

        for n in nums:
            xor ^= n
        
        lastOnBit = xor & (~(xor-1))

        for n in nums:
            if n & lastOnBit == 0:
                first ^= n
            else:
                sec ^= n
        return [first, sec]