class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
    # pushes the element val onto the end of the stack
    def push(self, val: int) -> None:
        if self.stack and self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)
        self.stack.append(val)
    
    # removes the element on the top of the stack
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    # gets the top element of the stack
    def top(self) -> int:
        return self.stack[-1]

    # retrieves the minimum element in the stack
    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
