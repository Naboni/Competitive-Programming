class QuickSort:
    def quick_sort(self, array, start, end):
        if start >= end: return
        p = self.partition(array, start, end)
        self.quick_sort(array, start, p-1)
        self.quick_sort(array, p+1, end)

    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end
        while True:
            while low <= high and array[high] >= pivot:
                high = high - 1
            while low <= high and array[low] <= pivot:
                low = low + 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break
        array[start], array[high] = array[high], array[start]
        return high

qs = QuickSort()
arr = [10,16,8,12,15,6,3,9,5]
qs.quick_sort(arr, 0, len(arr)-1) 
print(arr)