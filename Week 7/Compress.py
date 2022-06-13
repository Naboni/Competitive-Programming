class Solution:
    def compress(self, chars: List[str]) -> int:
        slow = 0
        fast = 0
        while fast < len(chars):
            chars[slow] = chars[fast]
            count = 1
            while fast + 1 < len(chars) and chars[fast] == chars[fast + 1]:
                count += 1
                fast += 1
            
            if count > 1:
                for c in str(count):
                    slow += 1
                    chars[slow] = c
                    
            slow += 1
            fast += 1
            
        return slow
