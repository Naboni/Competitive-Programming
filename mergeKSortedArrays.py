# TLE's
# class Solution:
# 	def mergeKArrays(self, arr: List[List[int]]) -> List[int]:
# 		while len(arr) > 1:
# 			arr1 = arr.pop()
# 			arr2 = arr.pop()
# 			arr.append(self.mergeTwo(arr1, arr2))
# 		return arr[0]

# 	def mergeTwo(self, arr1, arr2):
# 		i = j = 0
# 		result = []
# 		while i < len(arr1) and j < len(arr2):
# 			if arr1[i] <= arr2[j]:
# 				result.append(arr1[i])
# 				i += 1
# 			else:
# 				result.append(arr2[j])
# 				j += 1
# 		if i < len(arr1):
# 			result.extend(arr1[i:])
# 		else:
# 			result.extend(arr2[j:])
# 		return result
# TLE's
import heapq
class Solution:
	def mergeKArrays(self, arr: List[List[int]]) -> List[int]:
		heap = []
        for i in range(len(arr)):
            if arr[i]:
                heapq.heappush(heap, (arr[i][0], i, 0))
        result = []
        while heap:
            val, k, idx = heapq.heappop(heap)
            result.append(val)
            if arr[k] and idx+1 < len(arr[k]):
                heapq.heappush(heap, (arr[k][idx+1], k, idx+1))
        return result