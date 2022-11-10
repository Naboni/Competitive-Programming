class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        def helper(x, y):
            hashmap = {}
            for cur_x, cur_y in points:
                slope = inf if y == cur_y else (cur_x - x) / (cur_y - y)
                if slope == inf:
                    hashmap[slope] = hashmap.get(slope, 0) + 1
                else:
                    hashmap[slope] = hashmap.get(slope, 1) + 1
            return max(hashmap.values())
        for x, y in points:
            res = max(res, helper(x, y))
        return res