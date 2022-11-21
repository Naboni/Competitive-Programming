def solution(inputString):
    res = []
    stack = []
    for i in range(len(inputString)):
        if not stack:
            if inputString[i] != "(":
                res.append(inputString[i])
            else:
                stack.append("(")
        else:
            if inputString[i] == ")":
                curr = []
                while stack and stack[-1] != "(":
                    curr.append(stack.pop())
                stack.pop()
                j = 0
                while stack and j < len(curr):
                    stack.append(curr[j])
                    j += 1
                if not stack:
                    for i in curr:
                        res.append(i)
            else:
                stack.append(inputString[i])
    return "".join(res)

def solution(s):
    stack = []
    for char in s:
        if char != ")":
            stack.append(char)
        else:
            temp = []
            while stack[-1] != "(":
                temp.append(stack.pop())
            stack.pop()
            stack.extend(temp)
    return "".join(stack)