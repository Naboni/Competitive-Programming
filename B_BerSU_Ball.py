n  =  int(input())
boys = list(map(int, input().split()))
m  =  int(input())
girls = list(map(int, input().split()))
pair = 0
boys.sort()
girls.sort()
for i in range(n):
	for j in range(m):
		if abs(boys[i]-girls[j]) <= 1:
			pair+=1
			girls[j] = 6969
			break
print(pair)