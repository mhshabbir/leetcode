class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
            [-4,-1,0,3,10]
                 l r
                [0,1,3,4,10]
        """
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            left = abs(nums[l])
            right = abs(nums[r])
            if right > left:
                res.append(right**2)
                r -= 1
            else:
                res.append(left**2)
                l += 1
        finalRes = []
        for i in res[::-1]:
            finalRes.append(i)
        
        return finalRes
            