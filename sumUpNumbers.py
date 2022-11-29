s = input()
n = len(s)
i = 0
nums = 0
while i < n:
    num = []
    while i < n and s[i].isdigit():
        num.append(s[i])
        i += 1
    if num: 
        num = int("".join(num))
        nums += num
    i += 1
print(nums)