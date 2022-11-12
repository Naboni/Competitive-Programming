# Please Tell Me Why this is a wrong submission
# class Solution:
# 	def getSteppingNumbers(self, begin: int, end: int) -> List[int]:
# 		graph = [[] for _ in range(10)]
# 		for i in range(10):
# 			if i+1 < 10: graph[i].append(i+1)
# 			if i-1 >= 0: graph[i].append(i-1)
		
# 		left = str(begin)
# 		right = str(end)
# 		result = set()
# 		curr_len = len(left)
# 		while curr_len <= len(right):
# 			if curr_len == 1:
# 				x = begin
# 				while x < 11:
# 					result.add(x)
# 					x += 1
# 			else:
# 				for i in range(len(graph)):
# 					self.dfs(i, "", curr_len, graph, result, begin, end)
# 			curr_len += 1
# 		return list(result)
				
# 	def dfs(self, node, curr, size, graph, res, left, right):
# 		if len(curr) == size:
# 			if left <= int(curr) <= right:
# 				res.add(int(curr))
# 			return
# 		for neigh in graph[node]:
# 			self.dfs(neigh, curr + str(node), size, graph, res, left, right)