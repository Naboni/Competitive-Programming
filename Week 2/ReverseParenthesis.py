class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        string = list(s)
        for i in string:
            if i != ")":
                stack.append(i)
            else:
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack += temp
        return "".join(stack)

print(rev("(abcd)"))
print(rev("(u(love)i)"))
print(rev("(ed(et(oc))el)"))
