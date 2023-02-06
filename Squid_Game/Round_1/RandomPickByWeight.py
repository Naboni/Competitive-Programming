class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.length = len(w)
        for i in range(1, self.length):
            w[i] += w[i-1]
        self.s = self.w[-1]

    def pickIndex(self) -> int:
        seed = randint(1, self.s)
        left, right = 0, self.length-1
        while left < right:
            mid = (left + right) // 2
            if seed <= self.w[mid]:
                right = mid
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()