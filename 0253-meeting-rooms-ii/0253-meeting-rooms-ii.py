class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        startPtr = 0
        endPtr = 0

        count = 0
        result = 0

        while startPtr < len(start):
            if start[startPtr] < end[endPtr]:
                count += 1
                startPtr += 1
            else:
                count -= 1
                endPtr += 1

            result = max(result, count)

        return result
