import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        orgList = score[:]
        heapq._heapify_max(score)
        rank = {}
        for i in range(len(score)):
            if i == 0:
                rank[heapq._heappop_max(score)] = "Gold Medal"
            elif i == 1:
                rank[heapq._heappop_max(score)] = "Silver Medal"
            elif i == 2:
                rank[heapq._heappop_max(score)] = "Bronze Medal"
            else:
                rank[heapq._heappop_max(score)] = str(i+1)
       

        print(orgList)
        res = []
        for i in orgList:
            print(rank[i])
            res.append(rank[i])
        
        return res


