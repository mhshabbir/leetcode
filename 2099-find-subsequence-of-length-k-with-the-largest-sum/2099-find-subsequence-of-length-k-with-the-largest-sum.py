class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        maxHeap = [(-nums[i],i) for i in range(len(nums))]
        heapq.heapify(maxHeap)
        print(maxHeap)
        minHeap = []
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            num, index = (heapq.heappop(maxHeap))
            heapq.heappush(minHeap, (index, -num))
        
        for i in range(k):
            index, num = heapq.heappop(minHeap)
            res.append(num)

        return res
