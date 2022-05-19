class MyCircularDeque:

    def __init__(self, k: int):
        self.circularDeque = [None]*k
        self.length = k
        self.front = (k-1)%k
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.circularDeque[self.front] == None:
            self.circularDeque[self.front] = value
            self.front = (self.front - 1) % self.length
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.circularDeque[self.rear] == None:
            self.circularDeque[self.rear] = value
            self.rear = (self.rear + 1) % self.length
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        x = (self.front + 1) % self.length
        if self.circularDeque[x] == None:
            return False
        else:
            self.circularDeque[x] = None
            self.front = x
            return True

    def deleteLast(self) -> bool:
        x = (self.rear - 1) % self.length
        if self.circularDeque[x] == None:
            return False
        else:
            self.circularDeque[x] = None
            self.rear = x
            return True

    def getFront(self) -> int:
        x = (self.front + 1) % self.length
        if self.circularDeque[x] == None:
            return -1
        else:
            return self.circularDeque[x]

    def getRear(self) -> int:
        x = (self.rear - 1) % self.length
        if self.circularDeque[x] == None:
            return -1
        else:
            return self.circularDeque[x]

    def isEmpty(self) -> bool:
        if (self.rear - self.front) % self.length == 1 and self.circularDeque[(self.front + 1) % self.length] == None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.rear - self.front) % self.length == 1 and self.circularDeque[(self.front - 1) % self.length] != None:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
