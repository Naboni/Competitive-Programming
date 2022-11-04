for op in range(int(input())) :
	n = int(input())
	a = [(int (i)) for i in input().split()]
	cnt=0; q=[]
	for i in range(n) :
		while a[i]%2==0 :
			a[i]//=2; cnt+=1
		p = i+1; idx = 0
		while p%2==0 :
			p//=2;idx+=1
		if idx!=0 : q.append(idx)
	
	if cnt>=n : print(0);continue;
	n-=cnt; ans=0
	q.sort(reverse = True)
	
	for i in q :
		n-=i; ans+=1
		if n <=0 :
			break;
		
	if n>0 : print(-1)
	else: print(ans)

