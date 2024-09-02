class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        """
        [[1,2,4],[3,3,1]]
        [[4,2,1],[3,3,1]]
        """
        maxHeapGrid = [[-j for j in i] for i in grid]
        # n^2

        for i in maxHeapGrid:
            heapq.heapify(i)
            # n^2
        output = 0
        while len(maxHeapGrid[0]) > 0:
            # n
            maxArr = []
            for i in maxHeapGrid:
                maxArr.append(abs(heapq.heappop(i)))
                #nlogn
        # n * nlogn
        # n^2logn
            output += max(maxArr)
            # n
        
        return output

            