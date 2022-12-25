n = int(input())
arr = list(map(int, input().split()))

def solve():
    res = 0
    summ = sum(arr)
    if summ % 3 != 0 or n < 3:
        return res
    one_third = summ//3
    two_third = one_third * 2
    tot = curr = 0
    for i in range(n-1):
        tot += arr[i]
        if tot == two_third: 
            res += curr
        if tot == one_third: 
            curr += 1
    return res
print(solve())