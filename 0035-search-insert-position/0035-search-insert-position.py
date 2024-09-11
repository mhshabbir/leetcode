class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Goal:
        Return the index if target is found
        if not:
            return the sorted index where the target is suppose to go.

        nums: [1, 3, 5, 6] T: 2
        return 1

        run time: log n
                   l
        [-1, 0, 1, 3, 5, 6]    t = 2
                   ^ 
                r

        l = 3
        r = 3
        m = 3
        """

        # initial l, r
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r+l)//2
            if target < nums[mid]:
                r = mid - 1
            
            elif target > nums[mid]:
                l = mid + 1
                
            else:
                return mid
        
        if target > nums[mid]:
            return mid + 1
        else:
            return mid