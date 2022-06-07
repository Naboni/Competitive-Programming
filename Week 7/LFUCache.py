class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq

class LFUCache:

    def __init__(self, capacity: int):
        self.freq = defaultdict(OrderedDict) 
        self.d = {}
        self.minfreq = -1
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        n = self.d[key]
        od = self.freq[n.freq]
        del od[key]
        if not od and self.minfreq == n.freq:
            self.minfreq += 1
        n.freq += 1
        od = self.freq[n.freq]
        od[key] = n
        return n.value 

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.d[key].value = value
            return
        if self.capacity == 0:
            return
        if len(self.d) == self.capacity:
            od = self.freq[self.minfreq]
            k, v = od.popitem(last=False)
            del self.d[k]
        n = Node(value, 1)
        self.d[key] = n
        self.freq[1][key] = n
        self.minfreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
