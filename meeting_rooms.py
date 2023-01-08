class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        readyRooms, occupiedRooms, numMeetings = [], [], [0] * n
        for i in range(n):
            heappush(readyRooms, i)
        for meeting in meetings:
            while occupiedRooms and occupiedRooms[0][0] <= meeting[0]:
                heappush(readyRooms, heappop(occupiedRooms)[1])
            if readyRooms:
                roomId = heappop(readyRooms)
                numMeetings[roomId] += 1
                heappush(occupiedRooms, [meeting[1], roomId])
            else:
                room = heappop(occupiedRooms)
                room[0] += (meeting[1] - meeting[0])
                numMeetings[room[1]] += 1
                heappush(occupiedRooms, room)
        ans, maximum = 0, numMeetings[0]
        for i in range(n):
            if numMeetings[i] > maximum:
                maximum, ans = numMeetings[i], i
        return ans