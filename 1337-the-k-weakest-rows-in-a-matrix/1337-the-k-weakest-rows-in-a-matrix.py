class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        keep a hashmap maintaining the row:# of soldiers 

        """
        minHeap = []
        heapq.heapify(minHeap)

        for i in range(len(mat)):
            count = 0
            for one in mat[i]:
                if one == 1:
                    count += 1
                else:
                    break
            
            heapq.heappush(minHeap,(count, i))
            
        res = []
        for n in range(k):
            count, i = heapq.heappop(minHeap)
            res.append(i)
        
        return res

        # {0:2, 1:4, 2:1, 3:2, 4:5}
