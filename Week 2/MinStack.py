class MinStack:

    def __init__(self):
        self.stack = []
        
    # pushes the element val onto the stack
    def push(self, val: int) -> None:
        self.stack.append(val)
    
    # removes the element on the top of the stack
    def pop(self) -> None:
        self.stack.pop()

    # gets the top element of the stack
    def top(self) -> int:
        return self.stack[-1]

    # retrieves the minimum element in the stack
    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
