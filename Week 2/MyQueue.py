class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None
        
    # pushes to the back of the queue
    def push(self, x: int) -> None:
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    # removes from the front of the queue and returns it
    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    # returns element at the front of the queue
    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        return self.front
    
    # true if empty and false if not 
    def empty(self) -> bool:
        return (not self.stack1 and not self.stack2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
