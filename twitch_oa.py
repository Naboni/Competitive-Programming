from collections import defaultdict, deque

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

graph = defaultdict(list)
original = set()
for x, y in zip(arr1, arr2):
    original.add((x,y))
    graph[x].append(y)
    graph[y].append(x)

queue = deque([0])
visited = set([0])
result = 0
while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if nei not in visited:
            if (nei, node) not in original: 
                result += 1
            queue.append(nei)
            visited.add(nei)

print(result)
