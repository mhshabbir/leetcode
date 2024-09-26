class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Guass formula: n//2(n+1)
        1,2,3,4,5
        mid = 6/2 = 3
        levelSum = 3*4//2 = 6
        """
        l = 1
        r = n
        res = 0
        while l<=r:
            mid = (r+l)//2
            levelSum = (mid/2)*(mid+1)

            if levelSum > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res) 
        return res

        