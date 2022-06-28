class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for arr in matrix:
            heapq.heappush(heap,(arr[0],0,arr))
            
        while k > 0 and heap:
            val, idx, arr = heapq.heappop(heap)
            ans = val
            if idx+1<len(arr):
                heapq.heappush(heap,(arr[idx+1],idx+1,arr))
            k-=1
        return ans
