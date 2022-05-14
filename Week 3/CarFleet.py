class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpd = [[pos, spd] for pos, spd in zip(position, speed)]
        stack = []
        # reverse sorted order
        for pos, spd in sorted(posAndSpd)[::-1]:
            stack.append((target-pos)/spd)
            # choosing the car with lower speed
            if len(stack)>1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

print(car(12,[10,8,0,5,3],[2,4,1,1,3]))
print(car(10,[3],[3]))
print(car(100,[0,2,4],[4,2,1]))
