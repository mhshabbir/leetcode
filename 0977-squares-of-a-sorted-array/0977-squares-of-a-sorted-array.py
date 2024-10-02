class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
                   r
            [-4,-1,0,3,10]
                   l
            [0, 0, 0, 0, 0]    
        """
        res = [-1]*len(nums)
        l = 0
        r = len(nums)-1
        ptr = len(nums) - 1

        while l<=r:
            if abs(nums[l]) > abs(nums[r]):
                res[ptr] = abs(nums[l]**2)
                l += 1
                ptr -= 1
            else:
                res[ptr] = abs(nums[r]**2)
                r -= 1
                ptr -= 1
        
        return res
            