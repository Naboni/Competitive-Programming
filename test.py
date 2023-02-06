

n = int(input())
arr = list(map(int, input().split()))

prev = 0
rest = 0

for num in arr:
  if num == prev or num == 0:
    prev = 0
    rest += 1
  elif num < 3:
    prev = num
  elif prev:
    prev = 3 - prev

print(rest)
