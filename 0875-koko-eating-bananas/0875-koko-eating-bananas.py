
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        res = 0

        while left <= right:
            k = (left + right)//2
            
            hourPerPile = 0
            for pile in piles:
                hourPerPile += math.ceil(pile/k)
            # print(hourPerPile)
            if hourPerPile <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        
        return res


