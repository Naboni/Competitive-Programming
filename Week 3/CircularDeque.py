class MyCircularDeque:

    def __init__(self, k: int):
        self.circularDeque = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.circularDeque) < self.k:
            self.circularDeque = [value] + self.circularDeque
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.circularDeque) < self.k:
            self.circularDeque = se;f.circularDeque + [value]
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.circularDeque) > 0:
            self.circularDeque.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.circularDeque) > 0:
            self.circularDeque.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if len(self.circularDeque) > 0:
            return self.circularDeque[0]
        else:
            return -1

    def getRear(self) -> int:
        if len(self.circularDeque) > 0:
            return self.circularDeque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.circularDeque) == 0

    def isFull(self) -> bool:
        return len(self.circularDeque) == self.k


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
