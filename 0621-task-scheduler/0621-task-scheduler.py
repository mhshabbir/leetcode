class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = Counter(tasks)
        maxHeap = [-num for num in taskCounter.values()]
        heapq.heapify(maxHeap)
        q = deque()  # q[, -2 4]
        time = 0    # t=3
                    # h[-2 3]

        while maxHeap or q:
            time += 1
            if maxHeap:
                cur =1 + heapq.heappop(maxHeap)
                if cur:
                    q.append((cur, time+n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time  
