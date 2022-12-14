class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_stack = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.freq[val] + 1
        self.freq[val] = freq
        if freq > self.max_freq: self.max_freq = freq
        self.freq_stack[freq].append(val)

    def pop(self) -> int:
        val = self.freq_stack[self.max_freq].pop()
        if not self.freq_stack[self.max_freq]: self.max_freq -= 1
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()