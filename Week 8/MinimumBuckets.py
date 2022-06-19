class Solution:
    def minimumBuckets(self, street: str) -> int:
        count=0
        arr=list(street)
        for i in range(len(arr)):
            if arr[i]=="H":
                if i > 0 and arr[i-1]== "B":
                    continue
                if i+1<len(arr) and arr[i+1]==".":
                    arr[i+1]="B"
                    count+=1
                elif arr[i-1]=="." and i-1>=0:
                    arr[i-1]="B"
                    count+=1
                else:
                    return -1
        return count
