class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = defaultdict(int)
        visited = {}
        stack = []
        
        for i in s:
            freq[i] += 1
            visited[i] = False
            
        for i in s:
            if not visited[i]:
                while stack and stack[-1] > i and freq[stack[-1]] > 0:
                    visited[stack[-1]] = False
                    stack.pop()
                visited[i] = True
                stack.append(i)
            freq[i] -= 1
        
        return "".join(stack)
