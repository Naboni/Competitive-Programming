class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.power(x, n)
        else:
            return 1/self.power(x,-n)
        
    def power(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        temp = self.myPow(x,n//2)
        if n%2==0:
            return temp * temp
        else:
            return temp * temp * x

obj = Solution()
print(obj.myPow(2,10))
