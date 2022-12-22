from collections import deque

n, m = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

def solve(n, m, x1, y1, x2, y2):
    visited = set([(x1, y1)])
    queue = deque([(x1, y1, 0)])
    dir_vector = [1, 1]
    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == (x2, y2):
            return steps
        nx, ny = x+dir_vector[0], y+dir_vector[1]
        if (nx, ny) not in visited:
            if nx >= n or nx < 0:
                dir_vector[0] *= -1
            if ny >= m or ny < 0:
                dir_vector[1] *= -1
            queue.append((nx, ny, steps+1))
            visited.add((nx, ny))
    return -1

print(solve(n,m,x1,y1,x2,y2))