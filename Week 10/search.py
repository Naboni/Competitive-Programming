class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(arr):
            last = arr[-1]
            l, r = 0, len(arr)-1
            while l<=r:
                m = (l+r)//2
                if nums[m] > last:
                    l = m + 1
                else:
                    r = m - 1
            return l
        def binarySearch(arr, l, r):
            while l<=r:
                m = (l+r)//2
                if arr[m] == target:
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        pivot = findPivot(nums)
        leftSearch = binarySearch(nums, 0, pivot-1)
        if leftSearch != -1:
            return leftSearch
        else:
            return binarySearch(nums, pivot, len(nums)-1)
