class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
                       R
                     m
            [5,7,7,8,8,10]
                   L


        """

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                while nums[left] != target and left <= right:
                    if nums[left] != target:
                        left += 1

                while nums[right] != target and left <= right:
                    if nums[right] != target:
                        right -= 1
                        
                return [left, right]

        return [-1, -1]
                    