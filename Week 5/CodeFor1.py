import math
n, l, r = map(int, input().split())
def codeFor1(n):
    if n == 0 or n == 1:
        return [n]
    arr = codeFor1(n//2) + [n%2]
    return arr

def solve(arr, l, r):
    if len(arr) == 1 and l == 1 and r == 1:
        return arr[0]
    l-=1
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        x = pow(2, i) - 1
        if x >= r:
            break
        d = pow(2, i+1)
        j = 0 if l <= x else math.ceil((l-x)/d)
        k = math.ceil((r-x)/d)
        count += k - j 
    return count
    
##c = codeFor1(7)
##print(solve(c,2,5))
##c = codeFor1(10)
##print(solve(c,3,10))
