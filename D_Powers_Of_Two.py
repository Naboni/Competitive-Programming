import heapq


n, k = map(int,input().split())
binary = bin(n)[2:]
x = len(binary)
# print(binary)
on = []
for i in range(x):
    if binary[i] == "1":
        on.append(-2**(x-i-1))
# print(on)
if len(on) > k:
    print("NO")
    exit()
while len(on) < k:
    v = heapq.heappop(on)
    for i in range(2):
        heapq.heappush(on, v//2)
if sum(on) > n: print("NO")
else:
    print("YES")
    for i in on[::-1]:
        print(-i, end=" ")