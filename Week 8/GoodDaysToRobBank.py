class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        length = len(security)
        if time == 0:
            return range(length)
        output=[]
        x, y = 0, 0
        for i in range(1,length-time):
            x += 1 if security[i - 1] >= security[i] else -x
            y += 1 if security[i + time - 1] <= security[i + time] else -y
            
            if x >= time and y >= time:
                output.append(i)
        return output
