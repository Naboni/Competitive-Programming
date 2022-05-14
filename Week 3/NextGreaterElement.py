class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1HashMap = {n:i for i,n in enumerate(nums1)}
        output = [-1]*len(nums1)
        monoStack = []
        for i in range(len(nums2)):
            current = nums2[i]
            while monoStack and current > monoStack[-1]:
                value = monoStack.pop()
                index = nums1HashMap[value]
                output[index] = current
            if current in nums1HashMap:
                monoStack.append(current)
        return output

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))
