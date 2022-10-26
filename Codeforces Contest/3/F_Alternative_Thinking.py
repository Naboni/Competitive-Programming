n = int(input())
binary = input()

identical = 0
for i in range(1, n):
    if binary[i] == binary[i-1]:
        identical += 1
diff = n - identical

print(diff+min(2, identical))