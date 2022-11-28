class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        self.res = []

    def mergeSort(self, l, r):
        if l > r: return
        if l == r: return [self.arr[l]]
        mid = (l+r)//2
        left = self.mergeSort(l, mid)
        right = self.mergeSort(mid+1, r)
        return self.merge(left, right)

    def merge(self, arr1, arr2):
        res = []
        l1 = l2 = 0
        while l1 < len(arr1) and l2 < len(arr2):
            if arr1[l1] >= arr2[l2]:
                res.append(arr1[l1])
                l1 += 1
            else:
                res.append(arr2[l2])
                l2 += 1
            
        res.extend(arr1[l1:] or arr2[l2:])
        return res

n = int(input())
arr = list(map(int, input().split()))
ms = MergeSort(arr)

print(*ms.mergeSort(0, len(arr)-1))