from heapq import heappop, heappush


n = int(input())
lamps = []
for _ in range(n):
    lamps.append(list(map(int, input().split())))
benchs = list(map(int, input().split()))

pq = []
"""
1, Lamp on
2, Bench
3, Lamp off
"""
for x, y in lamps:
    heappush(pq, (x, 1))
    heappush(pq, (y, 3))

for bench in benchs:
    heappush(pq, (bench, 2))

lights = 0
result = []
while pq:
    v, t = heappop(pq)
    if t == 1:
        lights += 1
    elif t == 2:
        result.append(lights)
    elif t == 3:
        lights -= 1
print(*result)