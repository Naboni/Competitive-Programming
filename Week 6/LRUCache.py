class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        else:
            node = self.hashMap[key]
            self.put(key,node.value)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.removeNodeFromList(node)
            self.hashMap.pop(node.key)
            
        if len(self.hashMap)==self.capacity:
            node = self.tail.prev
            self.removeNodeFromList(node)
            self.hashMap.pop(node.key)   
        
        node = Node(key,value)
        self.hashMap[key] = node
        self.insertAtHead(node)
    
    def insertAtHead(self,node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        
    def removeNodeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
