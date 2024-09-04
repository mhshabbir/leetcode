class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount = [-num for num in amount]
        heapq.heapify(amount)
        operation = 0

        if amount[0] == 0:
            return operation
        while len(amount)>0:
            print(amount)
            if len(amount)>1:
                first = abs(heapq.heappop(amount))
                second = abs(heapq.heappop(amount))
                if first > 0 and second > 0:
                    first -= 1
                    second -= 1
                elif first > 0:
                    first -= 1
                else:
                    second -= 1
                
                if first != 0:
                    heapq.heappush(amount,-first)
                if second != 0:
                    heapq.heappush(amount, -second)
                operation += 1
            else:
                first = abs(heapq.heappop(amount))
                if first > 0:
                    first -= 1
                
                if first != 0:
                    heapq.heappush(amount,-first)
                    operation += 1
                else:
                    operation += 1

        return operation

                