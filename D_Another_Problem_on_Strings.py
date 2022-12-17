from collections import defaultdict
k=int(input())
s = input()
arr = []
for i in s:
    arr.append(int(i))
prefix = [0]*(len(arr))
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

visited=defaultdict(int)
visited[0] = 1
ans=0
for i in prefix:
    a=i-k
    if a in visited:
        ans+=visited[a]
    if i in visited:
        visited[i]+=1
    else:
        visited[i]=1

print(ans)
