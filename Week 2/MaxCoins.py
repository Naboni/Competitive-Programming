class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        c = len(piles) // 3
        s = piles[0:c]
        d = piles[c:len(piles)+1]
        a = []
        for i in range(len(d), 0, -2):
            n = d[i-2:i]
            a.append(n)
        ans = []
        for i in range(len(s)):
            x = [s[i],a[i][0],a[i][1]]
            ans.append(x)
        output = 0
        for i in range(len(ans)):
            output+=ans[i][1]        
        return output
