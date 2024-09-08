class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l = 0
        # r = len(nums) - 1
        # mid = (r + l)//2


        # while nums[mid] != target:
        #     # search left
        #     if target < nums[mid]:
        #         print(nums[mid])
        #         r = mid - 1
        #         mid = (r + l)//2

        #     # Search right
        #     else:
        #         l = mid + 1
        #         mid = (r + l)//2
            
        # return mid

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r+l)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1