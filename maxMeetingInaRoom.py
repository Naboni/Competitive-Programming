class Solution:
	def getMaxMeetings(self, meetings: List[Meeting]) -> int:
		meetings.sort(key=lambda x:x.end)
		res = 1
		prev = meetings[0]
		for i in range(1, len(meetings)):
			if meetings[i].start >= prev.end:
				res += 1
				prev = meetings[i]	
		return res