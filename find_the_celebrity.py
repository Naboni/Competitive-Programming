n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, (input().split()))))

def knows(a, b):
    return grid[a][b]

def findCelebrity(n):
    if n <= 1: return -1

    celeb = 0
    for i in range(n):
        if i != celeb and knows(celeb, i):
            celeb = i
    
    # check if everbody knows celeb or if celeb knows anybody (which will invalidate the case)
    for i in range(n):
        if i != celeb and not knows(i, celeb) and knows(celeb, i):
            return -1
    
    return celeb

print(findCelebrity(n))