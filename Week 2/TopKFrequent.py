from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        freqArr = x.most_common()
        kFreq = freqArr[:k]
        output = []
        for i in kFreq:
            output.append(i[0])
        return output

print(topK([1,1,1,2,2,3],2))
print(topK([1],1))
