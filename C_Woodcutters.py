n = int(input())

trees = []
for _ in range(n):
    trees.append(list(map(int, input().split())))
intervals = []
intervals.append([trees[0][0]-trees[0][1], trees[0][0]])

for i in range(1, len(trees)):
    left = trees[i][0] - trees[i][1]
    right = trees[i][0] + trees[i][1]
    if intervals[-1][1] < left:
        intervals.append([left, trees[i][0]])
    else:
        intervals.append([False, trees[i][0]])
res = 0
for x, y in intervals:
    if not x:
        res += 1
flag = False
if intervals[-1][0] == False:
    flag = True
print(res + flag)