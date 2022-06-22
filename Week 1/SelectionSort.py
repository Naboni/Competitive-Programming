import math
class Solution: 
    def select(self, arr, i):
        min_index = i
        for j in range(i, len(arr)-1):
            if arr[j+1] < arr[min_index]:
                min_index = j+1
        return min_index
            
    
    def selectionSort(self, arr,n):
        for i in range(n):
            min_index = self.select(arr, i)
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
