from collections import defaultdict
n = int(input())
s1 = input()
s2 = input()

x = ord("a")
par = defaultdict(int)
for i in range(26):
    par[x] = x
    x += 1

def find(i):
    if par[i] != i:
        par[i] = find(par[i])
    return par[i]

res = 0
for i in range(n):
    a, b = ord(s1[i]), ord(s2[i])
    findA, findB = find(a), find(b)
    if findA != findB:
        par[findA] = findB
        res+=1
print(res)
 
for i in par:
    if par[i] != i:
        print(chr(i),chr(par[i]))