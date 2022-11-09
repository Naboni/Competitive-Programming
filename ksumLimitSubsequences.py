arr = [1,2,1]
res = []
k = 2
def rec(ind, summ, path):
    if ind >= len(arr):
        if summ == k:
            res.append(tuple(path))
            return True
        return False
    path.append(arr[ind])
    if rec(ind+1, summ + arr[ind], path): return True
    path.pop()
    if rec(ind+1, summ, path): return True
    return False
rec(0, 0, [])
print(res)