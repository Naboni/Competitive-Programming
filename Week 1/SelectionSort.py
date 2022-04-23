class Solution: 
    def select(self, arr, i):
        return arr[i]
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
            minimum = i
            for j in range(i+1, n):
                if arr[j] < arr[minimum]:
                    minimum = j
            if minimum != i:
                arr[i], arr[minimum] = arr[minimum], arr[i]
        return arr
