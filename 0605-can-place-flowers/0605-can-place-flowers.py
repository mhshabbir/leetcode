class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n = n - 1
                return n <= 0

        for i, plot in enumerate(flowerbed):
            #begining
            if i == 0 and plot == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n = n - 1
            #end
            elif i == len(flowerbed)-1 and plot == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n = n - 1
            #middle
            elif plot == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n = n - 1
        return n <= 0