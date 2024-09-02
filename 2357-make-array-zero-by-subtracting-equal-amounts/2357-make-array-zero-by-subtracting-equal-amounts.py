class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        minHeap = [3, 5, 5]
        minValue = heappop - cur
                    5 - 5 = 0
        nums = [0,0,0,0,0]
        cur = heappop(minHeap) # cur = 0
        ops = 3

        """
        # minHeap = nums[:]
        # heapq.heapify(minHeap)
        # minValue = 0
        # operation = 0

        # while len(minHeap) > 0:
        #     cur = heapq.heappop(minHeap)
        #     # cur = 1
        #     if cur == 0:
        #         continue
        #     minValue = cur - minValue
        #     mv = 1 - 0 = 0
        #     mv = 1 - 0 = 0
        #     mv = 3 - 1 = 2
        #     mv = 5 - 3 = 2
        #     mv = 5 - 5 = 0

        #     if minValue > 0:
        #         operation += 1
        return len(set([num for num in nums if num > 0]))


            