class DetectSquares:

    def __init__(self):
        self.hashmap = {}
        
    def add(self, point: List[int]) -> None:
        px, py = point
        if (px, py) not in self.hashmap:
            self.hashmap[(px, py)] = 0
        self.hashmap[(px, py)] += 1

    def count(self, point: List[int]) -> int:
        res = 0 
        px, py = point
        for x,y in self.hashmap.keys():
            if abs(px - x) != abs(py - y) or px == x or py == y: continue
            if (x, py) in self.hashmap and (px, y) in self.hashmap:
                res += self.hashmap[(x,py)] * self.hashmap[(px,y)] * self.hashmap[(x,y)]
        return res 

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)