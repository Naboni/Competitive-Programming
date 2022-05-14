class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        monoStack = [] # our stack is pair: [index, temp]
        for index, temp in enumerate(temperatures):
            while monoStack and temp > monoStack[-1][1]:
                stackIndex, stackTemp = monoStack.pop()
                output[stackIndex] = index - stackIndex
            monoStack.append([index, temp])
        return output
print(dt([73,74,75,71,69,72,76,73]))
print(dt([30,40,50,60]))
print(dt([30,60,90]))
print(dt([30,30,90]))
