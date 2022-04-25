import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        x, output = [], []
        for i in range(len(points)):
            distance = math.sqrt(points[i][0]**2+points[i][1]**2)
            x.append([distance, points[i]])
        x.sort()
        ans = x[:k]
        for i in range(len(ans)):
            output.append(ans[i][1])
        return output
