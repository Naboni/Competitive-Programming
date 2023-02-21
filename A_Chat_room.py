s = input()
word = "hello"
i = 0

for char in s:
    if char == word[i]:
        i += 1
    if i >= len(word):
        break
if i >= len(word):
    print("YES")
else:
    print("NO")