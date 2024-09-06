class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        minHeap = []
        # Counter({5: 2, 4: 1})
        for i in counter.keys():
            count, key = counter[i], i
            minHeap.append((count, i))
        
        #  [(2, 5), (1, 4)]
        heapq.heapify(minHeap)
        for i in range(k):
            count, key = heapq.heappop(minHeap)
            count -= 1
            if count > 0:
                heapq.heappush(minHeap, (count, key))
        
        return len(minHeap)
            
        
