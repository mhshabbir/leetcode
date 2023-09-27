class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left = 0
        # right = len(nums) -1

        # while left <= right:
        #     mid = (left + right)//2
        #     if nums[mid] == target:
        #         return mid
        #     if nums[left] <= target and target < nums[mid]:
        #         right = mid - 1
        #     elif nums[mid] >= target and target >= nums[right]:
        #         left = mid
        
        # return -1

        # left = 0
        # right = len(nums)-1
        # mid = (left+right)//2

        # while left <= right:
        #     print(nums[left],nums[mid], nums[right] )
        #     if nums[left] <= target and target <= nums[mid]:     #0 < 7
        #         right = mid - 1
        #         mid = (left+right)//2
        #     elif nums[mid+1] >= target and target >= nums[right]:
        #         left = mid + 1
        #         mid = (left+right)//2
        #     elif target == nums[mid]:
        #         return mid
            
        # return -1
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2
            print(nums[left],nums[mid], nums[right] )
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[left]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
            




