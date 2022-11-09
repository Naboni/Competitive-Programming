def reverse(arr):
    if not arr: return []
    return reverse(arr[1:]) + [arr[0]]

arr = [1,2,3,4]
def reverse2(l, r):
    if l > r: return
    arr[l], arr[r] = arr[r], arr[l]
    reverse2(l+1,r-1)

n = len(arr)
def reverse3(i):
    x = n-i-1
    if i >= x: return
    arr[i], arr[x] = arr[x], arr[i]
    reverse3(i+1)

reverse3(0)
print(arr)