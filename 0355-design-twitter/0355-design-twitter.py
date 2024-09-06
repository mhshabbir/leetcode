class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followlist = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
        # {1: [0, 5], 2: [-1, 6]}
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followlist[userId].add(userId)
        for followeeId in self.followlist[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([time, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        print(minHeap)
        # print(res)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            print(res)
            if index>=0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush([time, tweetId, followeeId, index - 1])

        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followlist[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followlist[followerId]:
            self.followlist[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)