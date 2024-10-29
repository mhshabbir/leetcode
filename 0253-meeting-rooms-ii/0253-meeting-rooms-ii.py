class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        count = 0
        maxMeetingRoom = 0
        startPtr = 0
        endPtr = 0
        while startPtr < len(start):
            if start[startPtr] < end[endPtr]:
                startPtr += 1
                count += 1
            else:
                endPtr += 1
                count -= 1
            
            maxMeetingRoom = max(maxMeetingRoom, count)
        return maxMeetingRoom