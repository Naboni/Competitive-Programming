class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        bound = 2**31
        isNegative = True
        if ((dividend < 0 and divisor < 0) or 
            (dividend >= 0 and divisor >= 0)):
            isNegative = False
        dividend = left = abs(dividend)
        divisor  = div = abs(divisor)
        count, res = 1, 0
        while left >= divisor:
            left -= div
            res  += count 
            count += count
            div  += div
            if left < div:
                div = divisor          
                count = 1
        if isNegative:
            return max(-res, -bound)
        else:
            return min(res, bound-1)
        