import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        build a maxHeap
        """
        maxHeap = [-gift for gift in gifts]
        heapq.heapify(maxHeap)

        for i in range(k):
            pop = abs(heapq.heappop(maxHeap))
            sqr = math.floor(math.sqrt(pop))
            heapq.heappush(maxHeap, -sqr)
        print(maxHeap)

        return sum([abs(num) for num in maxHeap])
