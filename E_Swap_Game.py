def solve(arr):
    if arr[0] == 1:
        return True
    if min(arr) == arr[0]:
        return True
    return False
           
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if solve(arr):
        print("Bob")
    else:
        print("Alice")