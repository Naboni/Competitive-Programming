class Solution:
    def maxProfit(self, inventory, orders: int) -> int:
        MOD = 10**9+7
        l, r = 0, max(inventory)
        while r - l > 1:
            mid = (l + r) // 2
            sold = 0
            for i in inventory:
                if i > mid:
                    sold += i - mid
            if sold > orders:
                l = mid
            else:
                r = mid
        sold = 0
        res = 0
        for i in inventory:
            if i > r:
                sold += i - r
                res += (i + r + 1) * (i - r) // 2
        if sold < orders:
            res += (orders - sold) * r
        return res % MOD    