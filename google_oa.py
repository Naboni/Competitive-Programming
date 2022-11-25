s = input()
res = 0
for i in range(1, len(s)):
    if s[i] <= s[i-1]:
        res += 3
res += ord(s[-1])- ord("a") + 1
print(res - len(s))