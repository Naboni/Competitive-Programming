import random

class RandomizedSet:
    def __init__(self) -> None:
        self.indexMap = {}
        self.array = []

    def insert(self, val):
        if val in self.indexMap:
            return False
        self.indexMap[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val):
        if val not in self.indexMap:
            return False
        last, idx = self.array[-1], self.indexMap[val]
        self.array[-1], self.array[idx] = self.array[idx], self.array[-1]
        self.indexMap[last] = idx
        self.array.pop()
        self.indexMap.pop(val)
        return True
    
    def random(self):
        return random.choice(self.array)