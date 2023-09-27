class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = (left + right)//2
        runtime = len(nums) # 9
        while runtime != 0:
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
                mid = (right + left)//2
            elif target < nums[mid]:
                right = mid - 1
                mid = (right + left)//2

            runtime = runtime//2

        return -1 
