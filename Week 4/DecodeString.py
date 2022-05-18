class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop()
                x = ""
                while stack and stack[-1].isdigit():
                    x = stack.pop() + x
                stack.append(int(x)*subStr)
        return "".join(stack)
