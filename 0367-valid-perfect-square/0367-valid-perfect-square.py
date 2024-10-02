class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        if num is equal to 16 than building numbers of squares arr [1, 2, 3, 4]
                                                                    [1, 4, 9, 16]
                                                                    because 16 is the max num, stop building here.
        mid = l+7//2 = 16//2 = 8//2 = 4
        """
        #              r
        #        m
        # [1,2,3,4,5,6,7,8,9,10]
        #  l


        l = 0
        r = num
        while l<=r:
            mid = (l+r)//2
            if mid**2 < num:
                l = mid + 1
            elif mid**2 > num:
                r = mid - 1
            else:
                return True
        return False