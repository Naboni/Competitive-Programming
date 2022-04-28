class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2==1:
            return []
        
        x = [0]*(max(changed)+1)
        result = []
        
        for i in range(0, len(changed)):
            x[changed[i]]+=1
        
        if x[0]%2 == 0:
            n = x[0]//2
            for j in range(0,n):
                result.append(0)
        else:
            return []
        
        for i in range(1, len(x)):
            if x[i]==0:
                continue
            elif 2*i >= len(x):
                return []
            else:
                while x[i] > 0:
                    x[i]-=1
                    x[2*i]-=1
                    if x[2*i] < 0:
                        return []
                    else:
                        result.append(i)
        return result
