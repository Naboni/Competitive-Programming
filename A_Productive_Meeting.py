from heapq import heappop, heappush

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    heap = []
    for i, el in enumerate(arr):
        if el != 0:
            heappush(heap, (-el, i+1))
            
    res = []
    while len(heap) > 1:
        x, i = heappop(heap)
        y, j = heappop(heap)
        if x+1 != 0: heappush(heap, (x+1, i))
        if y+1 != 0: heappush(heap, (y+1, j))
        res.append([i, j])

    print(len(res)) 
    for i, j in res:
        print(i, j)