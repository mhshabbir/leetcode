class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums) -1
        # mid = (left + right)//2
        # while left <= right:
        #     print(nums[mid-1],nums[mid],nums[mid+1])
        #     if nums[mid+1] < nums[mid] and nums[mid+1] < nums[mid-1]:
        #         left = mid + 1
        #         mid = (left + right)//2
        #     elif nums[mid-1] < nums[mid] and nums[mid+1] > nums[mid-1]:
        #         right = mid - 1
        #         mid = (left + right)//2
        #     else:
        #         return nums[mid]    
        # left = 0
        # right = len(nums) -1
        # mid = (left + right)//2
        # res = 0
        # while left <= right:
        #     if nums[mid] >= nums[left]:
        #         res = nums[mid]
        #         left = mid + 1
        #         mid = (left + right)//2
        #     else:
        #         res = nums[mid]
        #         right = mid - 1
        #         mid = (left + right)//2
        #     res = min(nums[mid],res)

        # return res
        start , end = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = (start + end ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])


