class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right]:
                front, rear = s[left:right], s[left+1:right+1]    
                if front == front[::-1] or rear == rear[::-1]:
                    return True
                else:
                    return False
        return True 