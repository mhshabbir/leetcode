class Solution:
    def largestInteger(self, num: int) -> int:
        numList = [int(digit) for digit in str(num)]
        oddList = []
        evenList = []
        
        for i in numList:
            if i%2 == 0:
                evenList.append(-i)
            else:
                oddList.append(-i)
        
        heapq.heapify(oddList)
        heapq.heapify(evenList)

        res = []
        for i in numList:
            if i%2 == 0:
                res.append(abs(heapq.heappop(evenList)))
            else:
                res.append(abs(heapq.heappop(oddList)))

        return int("".join([str(digit) for digit in res]))