from collections import deque

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
x0, y0, x1, y1 = map(int, input().split())

visited = set()
dirs = [(-1,0), (1,0), (0,-1), (0,1)]    
dest = (x1, y1)
src = (x0, x1)
def rollFrom(pos):
    newStops = []
    for d in dirs:
        newX = pos[0]
        newY = pos[1]
        while(True): #rolling
            possibleNewX = newX + d[0]
            possibleNewY = newY + d[1]             
            if 0 <= possibleNewX < len(grid) and 0 <= possibleNewY < len(grid[0]) and (grid[possibleNewX][possibleNewY] != 1):
                newX = possibleNewX
                newY = possibleNewY
                continue
            else:
                break
        newStop = (newX, newY)
        if newStop == dest:
            return True
        newStops.append(newStop)
        
    visited.add(pos)
        
    for newStop in newStops:            
        if newStop not in visited:
            if rollFrom(newStop):
                return True                
    return False

       
print(rollFrom(src))