from cmath import inf
n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(str, input().split())))

def compile(arr, maxi):
    ops = {"+", "-"}
    stack = []
    mapp = {"+": lambda x,y:  x + y,
            "-": lambda x,y: x - y}
    curr, flag = None, False
    for i in range(len(arr)):
        if not stack and arr[i] not in ops:
            stack.append(int(arr[i]))
            flag = True
            maxi = max(maxi, int(arr[i]))
        elif arr[i] in ops and stack:
            if not curr:
                curr = arr[i]
            else:
                curr = None
                stack = []
            flag = False
        elif arr[i].isdigit():
            val = int(arr[i])
            maxi = max(maxi, val)
            if flag:
                stack = [val]
            else:
                num = stack.pop()
                x = mapp[curr](num, val)
                maxi = max(maxi, x)
                if x < num:
                    stack = [num]
                else:
                    stack.append(x)
                curr = None
            flag = True
    return maxi
res = -inf
for i in range(n):
    res = max(res, compile(grid[i], -inf))

for i in range(m):
    arr = []
    for j in range(n):
        arr.append(grid[j][i])
    res = max(res, compile(arr, -inf))
print(res)