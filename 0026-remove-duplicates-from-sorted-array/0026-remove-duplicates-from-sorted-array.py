class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #                        V
        # # num = [0,1,2,1,1,2,2,3,3,4]
        #              ^
        left = 0
        for right in range(len(nums)):
            if nums[right] != nums[left]:
                nums[left + 1] = nums[right]
                left += 1

        return left + 1