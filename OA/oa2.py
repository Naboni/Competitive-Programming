from cmath import inf
from collections import defaultdict
from heapq import heappop, heappush


n = int(input())
lamps = []
for _ in range(n):
    lamps.append(list(map(int, input().split())))

# brightnessMap = defaultdict(int)
# for lamp in lamps:
#     lampRange = [lamp[0]-lamp[1], lamp[0]+lamp[1]]
#     for i in range(lampRange[0], lampRange[1]+1):
#         brightnessMap[i] += 1

# result = 0
# for key in brightnessMap:
#     if brightnessMap[key] == 1:
#         result += 1

# print(result)

pq = []
mini, maxi = inf, -inf
for x, y in lamps:
    heappush(pq, (x-y, 0))
    heappush(pq, (x+y, 1))

lights = 0
result = []
prev = 0

while pq:
    v, t = heappop(pq)
    if t == 0:
        lights += 1
    else:
        lights -= 1
        
    if lights == 1:
        if prev == 0:
            result.append(v)
        else:
            result.append(v+1)
    elif prev == 1:
        if lights == 0:
            result.append(v+1)
        elif lights == 2:
            result.append(v)
    prev = lights

ans = []
for i in range(0, len(result), 2):
    ans.extend(range(result[i], result[i+1]))
print(ans)