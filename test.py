
for _ in range(int(input())):
  l=0
  r=10**9
  x=int(input())
  a=list(map(int,input().split()))
  for i in range(x-1):
    y=a[i]
    z=a[i+1]
    if(y>z):
      l=max(l,(z+y+1)//2)
    elif(y<z):
      r=min(r,(z+y)//2)
  if(l<=r):
    print(l)
  else:
    print(-1)