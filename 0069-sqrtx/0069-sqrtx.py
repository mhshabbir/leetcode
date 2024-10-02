class Solution:
    def mySqrt(self, x: int) -> int:
        """
              r=3        
            m=1  
        0,1,2,3,4,5,6,7,8
            l=2
        """
        l = 0
        r = x
        while l <= r:
            mid = (l + r)//2
            if mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
            else:
                return mid
        
        if mid * mid < x:
            return mid
        else:
            return mid - 1 