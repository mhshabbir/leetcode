class RecentCounter:

    def __init__(self):
        self.callQueue = deque()

    def ping(self, t: int) -> int:
        self.callQueue.append(t)
        
        while t - self.callQueue[0] > 3000:
            self.callQueue.popleft()
        
        return len(self.callQueue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)