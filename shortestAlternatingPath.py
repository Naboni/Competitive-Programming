class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)
        
        for edge in redEdges:
            redGraph[edge[0]].append(edge[1])
        
        for edge in blueEdges:
            blueGraph[edge[0]].append(edge[1])
        
        #print(redGraph)
        # 0 -> red
        # 1 -> blue
        
        q = deque([(0, 0, 0), (0, 0, 1)])
        ans = [[float(inf), float(inf)] for i in range(n)]
        ans[0][0], ans[0][1]  = 0, 0
        
        while q:
            node, dist, color = q.popleft()
            if color:
                # blue
                for neighbor in blueGraph[node]:
                    if ans[neighbor][color] < dist + 1:
                        continue
                    ans[neighbor][color] = dist + 1
                    q.append((neighbor, dist + 1, 0))
            
            else:
                for neighbor in redGraph[node]:
                    if ans[neighbor][color] < dist + 1:
                        continue
                    ans[neighbor][color] = dist + 1
                    q.append((neighbor, dist + 1, 1))
        
        ans2 = []
        for i in range(n):
            curr = min(ans[i])
            if curr == float(inf):
                ans2.append(-1)
            else:
                ans2.append(curr)
        
        return ans2
