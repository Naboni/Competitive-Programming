n = int(input())
arr = list(map(int, input().split()))
res, prev = 0, 0
for num in arr:
	if num == prev or num == 0:
		prev = 0
		res += 1
	elif num == 1 or num == 2:
		prev = num
	elif prev > 0 and num == 3:
		prev = 3 - prev
print(res)