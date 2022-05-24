from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums).most_common()[:k]
        output = []
        for i in range(len(count)):
            output.append(count[i][0])
        return output

print(topK([1,1,1,2,2,3],2))
print(topK([1],1))
