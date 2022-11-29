from collections import defaultdict

n = int(input())
filenames = []
for _ in range(n):
    filenames.append(input())

hashmap = defaultdict(int)
res = []
for name in filenames:
    if name not in hashmap: 
        hashmap[name] += 1
        res.append(name)
    else:
        new_name = name + "(" + str(hashmap[name]) + ")"
        hashmap[new_name] += 1
        hashmap[name] += 1
        res.append(new_name)

print(*res)