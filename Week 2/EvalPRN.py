import math
def evrpn(tokens):
    stack = []
    for i in range(len(tokens)):
        if tokens[i] == '+':
            stack.append(stack.pop()+stack.pop())
        elif tokens[i] == '*':
            stack.append(stack.pop()*stack.pop())
        elif tokens[i] == '-':
            stack.append(-1*(stack.pop()-stack.pop()))
        elif tokens[i] == '/':
            x = stack.pop()
            res = stack.pop()/x
            if res < 0:
                stack.append(math.ceil(res))
            else:
                stack.append(math.floor(res))
        else:
            stack.append(int(tokens[i]))
    return stack[0]

print(evrpn(["2","1","+","3","*"]))
print(evrpn(["4","13","5","/","+"]))
print(evrpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
