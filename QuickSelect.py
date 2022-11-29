class QuickSelect:
    def quickSelect(self, nums, l, r, k):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p < k:   return self.quickSelect(nums, p+1, r, k)
        elif p > k: return self.quickSelect(nums, l, p-1, k)
        else:       return nums[p]

qs = QuickSelect()
arr = [3,2,1,5,6,4]
k = 4
print(qs.quickSelect(arr, 0, len(arr)-1, k))