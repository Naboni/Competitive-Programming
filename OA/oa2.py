from collections import defaultdict


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

mapp = defaultdict(int)
for lamp in lamps:
    left, right = lamp[0]-lamp[1], lamp[0]+lamp[1]+1
    mapp[left] += 1
    mapp[right] -= 1

# print(mapp)
frequency = count = 0
lastkey = None
for key in mapp:
    if frequency == 1:
        if lastkey == None: count += 1
        else: count += key - lastkey
    frequency += mapp[key]
    lastkey = key
print(count)