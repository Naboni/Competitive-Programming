from cmath import inf
from collections import defaultdict
from heapq import heappop, heappush

n, m = map(int, input().split())

flights = []
for _ in range(m):
    flights.append(map(int, input().split()))

src, dst, k = map(int, input().split())

graph = defaultdict(list)
for x, y, w in flights:
    graph[x].append((y, w))

def djikstra():
    heap = [(0, src, 0)]
    prices = [inf] * n
    stops = [inf] * n
    
    while heap:
        price, node, stop = heappop(heap)
        if node == dst: return price
        if stop == k+1: continue
        for nei, wght in graph[node]:
            newPrice = price + wght
            newStop = stop + 1
            if newPrice < prices[nei] or newStop < stops[nei]:
                prices[nei] = newPrice
                stops[nei] = newStop
                heappush(heap, (newPrice, nei, newStop))
    return -1

print(djikstra())