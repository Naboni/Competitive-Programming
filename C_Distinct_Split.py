from collections import Counter, defaultdict

t = int(input())

def solve(n, s):
    res = 0
    count = Counter(s)
    hashmap = defaultdict(int)
    for el in s:
        hashmap[el] += 1
        count[el] -= 1
        if not count[el]: del count[el]
        ans = len(hashmap) + len(count)
        res = max(res, ans)
    return res

for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
