n = int(input())
nums = list(map(int, input().split()))
 
B = 0
C = 0
for i in nums:
    if i >=0:
        B+= i
    else:
        C += i
 
print(B - C)