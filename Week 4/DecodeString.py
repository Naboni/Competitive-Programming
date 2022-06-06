class Solution:
    def decodeString(self, s: str) -> str:
        output, num, stack = "", 0, []
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == "[":
                stack.append(output)
                stack.append(num)
                output, num = "", 0
            elif i == "]":
                prevNum = stack.pop()
                prevStr = stack.pop()
                output = prevStr + prevNum * output
            else:
                output+=i
        return output
