class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.freq = 1
        self.prev = self.next = None

class DLL:
    def __init__(self):
        self.head = self.tail = ListNode(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
        
    def insertAtHead(self, node):
        nxt = self.head.next
        self.head.next = nxt.prev = node
        node.prev, node.next = self.head, nxt
        self.size += 1
        
    def removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1
        
    def removeTail(self):
        tail = self.tail.prev
        self.removeNode(tail)
        return tail
    
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.freqTable = defaultdict(DLL)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.updateCache(self.cache[key], key, self.cache[key].val)

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        if key in self.cache:
            self.updateCache(self.cache[key], key, value)
        else:
            if len(self.cache) == self.cap:
                prevTail = self.freqTable[self.minFreq].removeTail()
                del self.cache[prevTail.key]
            node = ListNode(key, value)
            self.freqTable[1].insertAtHead(node)
            self.cache[key] = node
            self.minFreq = 1
    
    def updateCache(self, node, key, value):
        node = self.cache[key]
        node.val = value
        prevFreq = node.freq
        node.freq += 1
        self.freqTable[prevFreq].removeNode(node)
        self.freqTable[node.freq].insertAtHead(node)
        if self.freqTable[prevFreq].size == 0 and prevFreq == self.minFreq:
            self.minFreq += 1
        return node.val
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
