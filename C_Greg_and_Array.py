n, m, k = map(int, input().split())
 
array = list(map(int, input().split()))
 
L = []
R = []
D = []
 
for i in range(m):
 
    l, r, d = map(int, input().split())
    L.append(l)
    R.append(r)
    D.append(d)
 
    L[i] -= 1
 
queries = [0 for _ in range(m+1)]
 
 
for i in range(k):
    x, y = map(int, input().split())
    x -= 1
 
    queries[x] += 1
    queries[y] -= 1
 
c = 0
 
C = [0 for _ in range(n+1)]
 
for i in range(m):
    c += queries[i]
 
    C[L[i]] += D[i] * c
    C[R[i]] -= D[i] * c
 
c = 0
for i in range(n):
    c += C[i]
    array[i] += c
 
str_array = list(map(str, array))
 
print(" ".join(str_array))