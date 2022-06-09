class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}
        def sumOfFib(n):
            if not n in memo:
                memo[n] = sumOfFib(n-1) + sumOfFib(n-2)
            return memo[n]
        return sumOfFib(n)
        
