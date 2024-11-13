class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        wordLocation = {n:i for i,n in enumerate(list1)}

        leastIndexSum = float('inf')
        for i , n in enumerate(list2):
            if n in wordLocation:
                commonSum = i + wordLocation[n]
                if commonSum < leastIndexSum:
                    leastIndexSum = commonSum
                    word = []
                    word.append(n)
                elif commonSum == leastIndexSum:
                    word.append(n)
        return word
                