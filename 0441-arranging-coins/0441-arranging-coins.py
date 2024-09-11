class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
         n = 2:
         [1, 2, 2]

        """
        num = n
        for i in range(1, n+1):
            if i <= num:
                num -= i

            else:
                return i - 1
        