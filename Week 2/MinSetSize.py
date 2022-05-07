from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        sumOfMax = output = i = 0
        x = Counter(arr)
        ##  most_common() returns array of sets
        ##  with each set containing value and occurence  
        freqArr = x.most_common()
        while sumOfMax < len(arr)//2:
            sumOfMax+= freqArr[i][1]
            i +=1
            output+=1
        return output

print(minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(minSetSize([7,7,7,7,7,7]))
