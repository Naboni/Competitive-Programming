from collections import defaultdict


num = input()

res = []
l = 0
for r in range(len(num)):
    if num[r] != num[l]:
        res.append(str(r-l))
        res.append(num[l])
        l = r
res.append(str(r-l+1))
res.append(num[l])
print("".join(res))