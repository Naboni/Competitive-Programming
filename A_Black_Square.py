a1, a2, a3, a4 = map(int, input().split())
value = {1:a1, 2:a2, 3:a3, 4:a4}
s = input()
total = 0
for index in range(len(s)):
    total += value[int(s[index])]
print(total)
