class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        g = defaultdict(list)
        for a, b in edges:
            if vals[b] > 0:
                g[a].append(vals[b])
            if vals[a] > 0:
                g[b].append(vals[a])
        
        res = max(vals)
        for n, v in g.items():
            res = max(res, (vals[n] + sum(sorted(v, reverse=True)[:k])))
        return res