class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        
        """
        stairs = 0
        for i in range(1,n+1):
            if n - i < 0:
                return stairs
            else:
                stairs += 1
                n -= i
            
        return stairs
        