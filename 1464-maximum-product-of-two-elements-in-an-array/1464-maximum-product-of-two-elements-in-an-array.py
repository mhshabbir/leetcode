class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxHeap = [-s for s in nums]
        heapq.heapify(maxHeap)

        return ((abs(maxHeap[0])-1) * (abs(maxHeap[1])-1))