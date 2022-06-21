class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        heap = []
        for key in hashmap:
            heapq.heappush(heap, (-hashmap[key], key))
        
        output = []
        for _ in range(k):
            popped = heapq.heappop(heap)
            output.append(popped[1])
        
        return output
