class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        stones = [2,4,1,1]
        stone1 = 8
        stone2 = 7
        newstone = 8 - 7 = 1

        """
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            print(maxHeap)
            stone1, stone2 = -(heapq.heappop(maxHeap)), -(heapq.heappop(maxHeap))
            print(stone1, stone2)
            if stone1 > stone2:
                newStone = stone1 - stone2
                heapq.heappush(maxHeap, -newStone)
            # elif stone2 > stone1:
            #     newStone = stone2 - stone1
            #     heapq._heappush_max(stones, newStone)
        print(maxHeap)
        if len(maxHeap) == 0:
            heapq.heappush(maxHeap, 0)
            return maxHeap[0]
        else:
            
            return -maxHeap[0]