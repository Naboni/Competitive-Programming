from collections import defaultdict, deque

def bfs(graph):
    queue = deque([0])
    visited = set([0])
    dist = [0] * n
    while queue:
        curr = queue.popleft()
        for i in graph[curr]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
                dist[i] = dist[curr] + 1
    return dist[n-1] if dist[n-1] != 0 else -1

n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

print(graph)

if n - 1 in graph[0]:
    for i in range(n):
        graph[i] = [j for j in range(n) if j not in graph[i] and j != i]

print(graph)


print(bfs(graph))
				  		  		  			 	    		 	  		