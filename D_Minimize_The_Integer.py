t = int(input())

def solve(s):
    even, odd = [], []

    for el in s:
        if int(el) % 2 == 0: even.append(int(el))
        else: odd.append(int(el))

    res = []
    i = j = 0
    while i < len(even) and j < len(odd):
        if even[i] < odd[j]:
            res.append(even[i])
            i += 1
        else:
            res.append(odd[j])
            j += 1
    res.extend(even[i:])
    res.extend(odd[j:])
    return res

for _ in range(t):
    s = input()
    ans = solve(s)
    for el in ans:
        print(el, end="")
    print()