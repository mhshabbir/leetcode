import heapq
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        minheap = []
        result = 0

        def getPower(num):
            count = 0
            while num != 1:
                if num % 2 == 0:
                    num = num / 2
                else:
                    num = 3 * num + 1
                count += 1
            return count

        for i in range(lo, hi + 1):
            minheap.append((getPower(i), i))
        
        heapq.heapify(minheap)

        for i in range(k):
            result = heapq.heappop(minheap)
        
        return result[1]