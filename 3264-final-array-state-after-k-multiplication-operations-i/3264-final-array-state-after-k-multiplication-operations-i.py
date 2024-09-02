class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = nums[:]
        heapq.heapify(minHeap)

        for i in range(k):
            pop = heapq.heappop(minHeap)
            heapq.heappush(minHeap, nums[nums.index(pop)] = pop*multiplier)

        return nums
        