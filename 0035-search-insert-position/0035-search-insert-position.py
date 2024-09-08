class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        l = 0
        r = 0
        m = 0
        """
        #           m
        # # nums = [1,3,5,6,7,8,9,10]
        #           l 
        #           r
        l, r = 0, len(nums)-1
        while l<=r:
            m = (r+l)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        if target > nums[m]:
            return m + 1
        else:
            return m 
                 