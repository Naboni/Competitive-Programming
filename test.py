arr = [1,1,2,1]
k = 2
def rec(ind, summ, path):
    if ind >= len(arr):
        if summ == k:
            return 1
        return 0
    path.append(arr[ind])
    x = rec(ind+1, summ + arr[ind], path)
    path.pop()
    y = rec(ind+1, summ, path)
    return x + y

print(rec(0, 0, []))