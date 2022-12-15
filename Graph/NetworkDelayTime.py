class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, time in times:
            graph[a].append((time, b))
        return self.djikstra(k, graph, n)

    def djikstra(self, node, graph, nodes):
        heap = [(0, node)]
        visited = defaultdict(lambda:inf)
        while heap:
            w, n = heappop(heap)
            if w >= visited[n]: continue
            visited[n] = w
            for time, nei in graph[n]:
                heappush(heap, (time+w, nei))
        return max(visited.values()) if len(visited) == nodes else -1