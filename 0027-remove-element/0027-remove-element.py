class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            step 1: remove the element from the list
            return the remaining elements

        """

        for i in range(len(nums)-1,-1, -1):
            if nums[i] == val:
                nums.remove(nums[i])
            print(nums)
        return len(nums)