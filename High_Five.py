from collections import defaultdict
from heapq import heappop, heappush

arr = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

def highFive(items):
    score_map = defaultdict(list)
    for x, y in items:      
        heappush(score_map[x], y)
        if len(score_map[x]) > 5:
            heappop(score_map[x])
    result = []
    for key, value in sorted(score_map.items()):
        result.append([key, sum(value)//5])
    return result

print(highFive(arr) == [[1,87],[2,88]])