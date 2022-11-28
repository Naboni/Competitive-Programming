class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int("".join(map(str,(self.mergeSort(nums, 0, len(nums)-1))))))

    def mergeSort(self, nums, left, right):
        if left > right: return
        if left == right: return [nums[left]]
        mid = (left + right) // 2
        arr1 = self.mergeSort(nums, left, mid)
        arr2 = self.mergeSort(nums, mid+1, right)
        return self.merge(arr1, arr2)

    def merge(self, arr1, arr2):
        result = []
        ptr1 = ptr2 = 0
        while ptr1 < len(arr1) and ptr2 < len(arr2):
            if self.compare(arr1[ptr1], arr2[ptr2]):
                result.append(arr1[ptr1])
                ptr1 += 1
            else:
                result.append(arr2[ptr2])
                ptr2 += 1
        result.extend(arr1[ptr1:] or arr2[ptr2:])
        return result
    
    def compare(self, num1, num2):
        num1 = str(num1)
        num2 = str(num2)
        return num1 + num2 > num2 + num1