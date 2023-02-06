class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 0, 1)])
        while q:
            res, pos, vel = q.popleft()
            if pos == target:
                return res
            q.append((res + 1, pos + vel, 2 * vel))            
            if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
                q.append((res + 1, pos, -vel / abs(vel)))