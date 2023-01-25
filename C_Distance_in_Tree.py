n,k=[int(i) for i in input().split()]
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
	a,b=[int(i) for i in input().split()]
	tree[a].append(b)
	tree[b].append(a)
	
dp=[[0 for _ in range(k+1)]  for _ in range(n+1)]
stack=[(1,0)]
idx=[0]*(n+1)
dp[1][0]=1
ans=0

while stack:
	x,p=stack[-1]
	y=idx[x]

	if y==len(tree[x]):

		if x==1:
			break
		stack.pop()

		for i in range(k,0,-1):
			dp[x][i]=dp[x][i-1]
		dp[x][0]=0

		for i in range(k):
			ans+=dp[p][i]*dp[x][k-i]
			dp[p][i]+=dp[x][i]
	else:
		z=tree[x][y]
        
		if z!=p:
			stack.append((z,x))
			dp[z][0]=1
		idx[x]+=1
 
print(ans) 
	