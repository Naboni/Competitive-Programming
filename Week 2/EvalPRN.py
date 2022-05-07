import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        result = []
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                result.append(tokens[i])
            else:
                if tokens[i] == "+":
                    calc = int(result[-2]) + int(result[-1])
                elif tokens[i] == "-":
                    calc = int(result[-2]) - int(result[-1])
                elif tokens[i] == "/":
                    if int(result[-2]) / int(result[-1]) < 0:
                        calc = math.ceil(int(result[-2]) / int(result[-1]))
                    else:
                        calc = int(result[-2]) // int(result[-1])
                elif tokens[i] == "*":
                    calc = int(result[-2]) * int(result[-1])
                result.pop()
                result.pop()
                result.append(calc)
        return result[0]

print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
