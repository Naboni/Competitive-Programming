class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        hours = [8,4,2,1]
        mins = [32,16,8,4,2,1]
        res = set()
        def helper(time, h, m, on):
            if on == turnedOn:
                # f'{i:05d}
                res.add(":".join(time))
                return
            for i in range(h, len(hours)):
                currHour = int(time[0]) + hours[i]
                if currHour < 12:
                    helper([str(currHour), time[1]], i+1, m, on+1)
            
            for i in range(m, len(mins)):
                currMin = int(time[1]) + mins[i]
                if currMin < 60:
                    helper([time[0], f'{currMin:02d}'], h, i+1, on+1)
        helper(["0","00"], 0, 0, 0)
        return res