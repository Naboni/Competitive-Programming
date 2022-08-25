class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q1, q2 = deque(), deque()
        n = len(senate)
        
        for i, senator in enumerate(senate): 
            if senator == 'R':
                q1.append(i)
            else:
                q2.append(i)
        
        while q1 and q2:
            x, y = q1.popleft(), q2.popleft()
            
            if x < y:
                q1.append(x + n)
            else:
                q2.append(y + n)
                 
        if q1:
            return "Radiant"
        return "Dire"
