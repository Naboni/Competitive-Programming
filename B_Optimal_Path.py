# from collections import deque
# from heapq import heappop, heappush


t = int(input())

# def solve(n, m):
#     visited = set([(1,1)])
#     heap = [[1,1,1]]
#     while heap:
#         steps, r, c = heappop(heap)
#         if (r,c) == (n,m): return steps
#         for dr, dc in [(1,0),(0,1)]:
#             nr, nc = r+dr, c+dc
#             if 1<=nr<=n and 1<=nc<=m and (nr, nc) not in visited:
#                 heappush(heap, (steps + (nr-1)*m + nc, nr, nc))
#                 visited.add((nr, nc))
#     return -1

for _ in range(t):
    n, m = map(int, input().split())
    
    top = m * (m-1) // 2
    right = m * (n * (n+1)) // 2

    print(top + right)
