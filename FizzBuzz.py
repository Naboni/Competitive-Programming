class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1, n+1):
            if (i % 3 == 0):
                if(i % 5 == 0):
                    output.append("FizzBuzz")
                else:
                    output.append("Fizz")
            elif (i % 5 == 0):
                output.append("Buzz")
            else:
                output.append(str(i))
        return output