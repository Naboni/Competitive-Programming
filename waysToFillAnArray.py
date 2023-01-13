class Solution:
    def __init__(self):
        self.dp = {}
        self.fac = {}
        
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        def factors(n):
            if self.fac.get(n) is None:
                ret = []
                for i in range(2, n):
                    if n % i == 0:
                        ret.append(i)
                self.fac[n] = ret
            return self.fac[n]
        
        def ways(n):
            if self.dp.get(n) is None:
                facs = factors(n)
                if not facs:
                    return {1 : 1}
                ret = defaultdict(int)
                ret[1] = 1
                for f in facs:
                    for k, v in ways(n // f).items():
                        ret[k + 1] += v
                
                self.dp[n] = ret
                
            return self.dp[n]
        
        ret = []
        for q in queries:
            if q[0] == 1 or q[1] == 1:
                ret.append(1)
                continue
            w = ways(q[1])
            # print(w)
            cur = 0
            for k, v in w.items():
                if k > q[0]:
                    continue
                cur = (cur + comb(q[0], k) * v) % 1000000007
            ret.append(cur)
            
        return ret