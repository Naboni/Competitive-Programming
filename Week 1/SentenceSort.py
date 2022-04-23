class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr1, arr2 = [], []
        
        for i in s.split(" "):
            arr1.append(i)
        for i in range(len(arr1)):
            for j in range(len(arr1)-1):
                if arr1[j][-1] > arr1[j+1][-1]:
                    arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
        for i in arr1:
            i = i.replace(i[-1], "")
            arr2.append(i)
        return " ".join(arr2)
                    
