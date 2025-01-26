class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastend = output[-1][1]

            if start <= lastend:
                output[-1] = [output[-1][0], max(end,lastend)]
            else:
                output.append([start, end])
        
        return output


