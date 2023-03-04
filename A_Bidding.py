from collections import defaultdict

n, d = map(int, input().split())

bids = defaultdict(list)
for i in range(n):
    id, amount, timestamp = map(int, input().split())
    bids[amount].append((id, timestamp))

res = None
idle_time = 0
while True:
    if bids:
        max_bid = max(bids.keys())
    else: break

    res = bids[max_bid].pop(0)
    if not bids[max_bid]: del bids[max_bid]
    idle_time = res[1]
    if idle_time == d: break

print(res[0])
