binary = input()
n = len(binary)

res = []
for i in range(0, n, 8):
    b = int(binary[i:i+8], 2)
    c = chr(b)
    res.append(c)
print("".join(res))