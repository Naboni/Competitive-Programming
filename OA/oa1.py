s = input()
k = int(input())

def sumDigit(chars):
    res = 0
    for i in chars:
        res += int(i)
    return str(res)

while len(s) > k:
    temp = []
    for i in range(0, len(s), k):
        temp.append(sumDigit(s[i:i+k]))
    s = "".join(temp)

print(s)