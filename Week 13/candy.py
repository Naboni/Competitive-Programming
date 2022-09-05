class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        
        left, right = [1] * n, [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            if ratings[n - i - 1] > ratings[n - i]:
                right[n-i-1] = right[n - i] + 1
        
        candy = 0
        for i in range(n):
            candy += max(left[i], right[i])
        
        return candy
