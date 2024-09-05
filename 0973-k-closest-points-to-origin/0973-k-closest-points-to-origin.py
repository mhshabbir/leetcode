import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for i, n in enumerate(points):
            element = math.sqrt(math.pow(n[0],2)+math.pow(n[1], 2))
            heapq.heappush(minHeap, (element, i))
        res = []
        for i in range(k):
            element, index = heapq.heappop(minHeap)
            res.append(points[index])
        
        return res
