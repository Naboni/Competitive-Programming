from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr).most_common()
        countSum = output = 0
        for i in range(len(count)):
            if countSum < (len(arr)//2):
                countSum += count[i][1]
                output += 1
        return output
print(minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(minSetSize([7,7,7,7,7,7]))
