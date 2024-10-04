class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        """    
                     r
               m m+1      
        [1,2,1,3,5,6,4]
             m-1
         l
        """
        def isPeak(index):
            # print(index)
            if index == 0 and nums[index+1] < nums[index]:
                return True
            elif index == len(nums) - 1 and nums[index - 1] < nums[index]:
                # print("second if")
                return True
            elif nums[index - 1] < nums[index] > nums[index + 1]:
                return True
            else:
                return False

        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return 0

        while left <= right:
            mid = (right + left)//2
            # print(mid)
            if isPeak(mid):
                return mid
            # look left
            elif mid-1 >= 0 and nums[mid] < nums[mid-1]:
                right = mid - 1
            else:
                left = mid + 1
        
        
