n = int(input())
colors = list(map(int, input().split()))

compressed = []
for color in colors:
    if not compressed or compressed[-1] != color:
        compressed.append(color)

length = len(compressed)
dp1 = []
dp2 = [0] * (length+1)

for i in range(1, length):
    dp = []
    for j in range(length-i):
        if compressed[j] == compressed[j+i]:
            dp.append(min(dp2[j+1], dp1[j+1], dp2[j]) + 1)
        else:
            dp.append(min(dp2[j+1], dp2[j]) + 1)
    dp1, dp2 = dp2, dp
print(dp2[0])
 
