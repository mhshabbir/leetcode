class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        nums = [1,3,12,0,0]
                      ^  ^

        """
        left = 0
        for r in range(len(nums)):
            while nums[left] != 0 and left < len(nums)-1:
                left += 1
            if nums[r] != 0 and r > left:
                nums[left], nums[r] = nums[r], nums[left]
                left += 1
            

                         