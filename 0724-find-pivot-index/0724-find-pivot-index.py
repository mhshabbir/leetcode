class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        [1,7,3,6,5,6]
             ^
        total = 28
        leftsum = 11
        rightsum = 11
        cur = 6
            
        if (total - cur) == (rightsum + leftsum - cur):
            pivot = i

        """
        total = sum(nums)
        rightsum = total
        leftsum = 0

        for i,cur in enumerate(nums):
            rightsum -= cur
            if leftsum == rightsum:
                return i
            else:
                leftsum += cur
        return -1
