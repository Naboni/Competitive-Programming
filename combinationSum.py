class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.combinations([], 0, 0, candidates, target)
        return self.result

    def combinations(self, path, index, total, candidates, target):
        if total > target:
            return
        if total == target:
            self.result.append(path)
            return
        for i in range(index, len(candidates)):
            self.combinations(path+[candidates[i]], i, total+candidates[i], candidates, target)