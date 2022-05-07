class MyQueue:

    def __init__(self):
        self.queue = []
        
    # pushes to the back of the queue
    def push(self, x: int) -> None:
        self.queue.append(x)

    # removes from the front of the queue and returns it
    def pop(self) -> int:
        return self.queue.pop(0)

    # returns element at the front of the queue
    def peek(self) -> int:
        return self.queue[0]
    
    # true if empty and false if not 
    def empty(self) -> bool:
        return True if len(self.queue)==0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
