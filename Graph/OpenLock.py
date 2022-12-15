class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        deads = set(deadends)
        while queue:
            lock, steps = queue.popleft()
            if lock in deads: continue
            if lock == target: return steps
            for i in range(4):
                current = int(lock[i])
                add, sub = (current + 1) % 10, (current - 1) % 10
                addLock = lock[:i] + str(add) + lock[i+1:] 
                subLock = lock[:i] + str(sub) + lock[i+1:]
                if addLock not in visited:
                    queue.append((addLock, steps+1))
                    visited.add(addLock)
                if subLock not in visited:
                    queue.append((subLock, steps+1))
                    visited.add(subLock)
        return -1