class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        stringifiedArr = sorted([str(num) for num in nums])
        current = [stringifiedArr[0]]
        
        for i in range(1, len(nums)):
            x, y = stringifiedArr[i], current[-1]
            if x+y < y+x:
                stringifiedArr[i-len(current)] = x
                stringifiedArr[i] = y
            elif x+y == y+x:
                current.append(x)
            else:
                current = [x]
        result = ''.join(reversed(stringifiedArr))
        if int(result) > 0:
            return result
        else:
            return '0'
