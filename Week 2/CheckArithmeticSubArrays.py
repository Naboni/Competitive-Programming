class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            seq = nums[l[i]:r[i]+1]
            seq.sort()
            count = 0
            for i in range(1,len(seq)-1):
                if (seq[i+1] - seq[i]) == (seq[1] - seq[0]):
                    count+=1
                else:
                    count=0
                    break
            if len(seq)-2 == count:
                answer.append(True)
            else:
                answer.append(False)
        return answer
