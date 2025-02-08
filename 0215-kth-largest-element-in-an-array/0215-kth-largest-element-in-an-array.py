import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        result = None
        for i in range(k):
            result = heapq.heappop(maxHeap)
        
        return -result
