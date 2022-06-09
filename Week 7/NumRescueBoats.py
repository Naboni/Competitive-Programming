class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort(reverse=True)
        i,j,count=0,n-1,0
        
        while i<=j:
            sum=people[i]+people[j]
            if  sum>limit:
                i+=1
            else :
                i+=1
                j-=1
            count+=1
        return count
