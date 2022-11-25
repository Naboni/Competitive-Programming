from cmath import inf
from heapq import heappop, heappush

# Djikstra Template
class Djikstra:
    def djikstra(n, graph, source, target):
        visited = [False] * n
        distance = [inf] * n

        heap = [(0, source)]
        distance[source] = 0

        while heap:
            dist, node = heappop(heap)
            if node == target: return dist
            if visited[node]: continue
            visited[node] = True
            for nei, wght in graph[node]:
                newDist = dist + wght
                if not visited[nei] and newDist < distance[nei]:
                    distance[nei] = newDist
                    heappush(heap, (distance[nei], nei))

        return -1