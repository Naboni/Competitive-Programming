from collections import defaultdict


class SumQuery:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = defaultdict(int)
        for i in b:
            self.b[i] += 1

    def solve(self, query):
        if len(query) == 3:
            self.a[query[1]] = query[2]
            return
        
        count = 0
        for num in self.a:
            # print(query[1] - num)
            if query[1] - num in self.b:
                # print("ye")
                count += self.b[query[1]-num]
        return count


# obj = SumQuery([2,3], [1,2,2])

# print(obj.solve([1,4]))
# print(obj.solve([0,0,3]))
# print(obj.solve([1,5]))

obj = SumQuery([3,4], [1,2,3])

print(obj.solve([1,5]))
print(obj.solve([0,0,1]))
print(obj.solve([1,5]))