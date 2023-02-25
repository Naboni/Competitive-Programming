a = input()
b = input()

def solve(a, b):
    if a == b: return True
    if len(a) % 2 == 1: return False
    half = len(a)//2
    a1, a2 = a[0:half], a[half:]
    b1, b2 = b[0:half], b[half:]
    return (solve(a1, b2) and solve(a2, b1)) or (solve(a1, b1) and solve(a2, b2))

if solve(a, b):
    print("YES")
else:
    print("NO")