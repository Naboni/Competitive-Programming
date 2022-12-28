class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def count(val, divisor):
            return val - val//divisor
        left = 1
        right = 10**10
        divisor3 = lcm(divisor1, divisor2)
        while left <= right:
            mid = (left+right)//2
            count1 = count(mid, divisor1)
            count2 = count(mid, divisor2)
            count12 = count(mid, divisor3)
            if count1 < uniqueCnt1 or count2 < uniqueCnt2 or (count12 < uniqueCnt1 + uniqueCnt2):
                left = mid + 1
            elif count1 >= uniqueCnt1 and count2 >= uniqueCnt2 and (count12 == uniqueCnt1 + uniqueCnt2):
                if mid % divisor3 == 0:
                    mid -= 1
                return mid
            else:
                right = mid - 1
        
        return left