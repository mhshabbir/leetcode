class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
                     R=4
                       M=2
        potions = [1,2,3,4,5]
                     L=0
                  pair = 5 * 3 = 15 
                  maxPair = 5 - 1 = 5-2
        spells = [5,3]

        [5,10,15,20,25]

        """
        potions.sort()
        res = []
        for spell in spells:
            left = 0
            right = len(potions) - 1
            maxPair = 0
            while left <= right:
                mid = (left + right)//2
                pair = spell*potions[mid]
                if pair < success:
                    left = mid + 1
                else: 
                    maxPair = max((len(potions) - mid), maxPair)
                    right = mid - 1
            res.append(maxPair)
        return res