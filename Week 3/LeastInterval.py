class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        maximum = 0
        for i in tasks:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            maximum = max(maximum, count[i])
        output = (maximum-1)*(n+1)
        for i in count.values():
            if i == maximum:
                output+=1
        return max(output, len(tasks))
    
print(li(["A","A","A","B","B","B"],2))
print(li(["A","A","A","B","B","B"],0))
print(li(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
