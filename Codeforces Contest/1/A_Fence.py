n, k = map(int, input().split())
planks = list(map(int, input().split()))
prefix = [0] * n
for i in range(n):
    if i == 0: 
        prefix[0] = planks[0]
    else:
        prefix[i] = prefix[i-1] + planks[i]
    
mini = float("inf")
index = 0
ans = 0
for i in range(n-k+1):
    if i == 0:
        index = prefix[i+k-1]
    else:
        index = prefix[i+k-1] - prefix[i-1]
    
    if index < 0:
        index = -1 * index
    if index < mini:
        mini = index
        ans = i

print(ans+1)