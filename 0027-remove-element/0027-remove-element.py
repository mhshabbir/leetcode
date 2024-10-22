class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #                 V
        # nums = [2,2,2,3]
        #             ^
        # left = 0
        # right = 0
        # while right < len(nums):
        #     if nums[left] == val or nums[right] == val:
        #         while right < len(nums) - 1 and nums[right] == val:
        #             right += 1
        #         nums[left] = nums[right]
        #     else:
        #         nums[left] = nums[right]

        #     left += 1
        #     right += 1
        # return left + 1
        for i in range(len(nums)-1,-1, -1):
            if nums[i] == val:
                nums.remove(nums[i])
            print(nums)
        return len(nums)
