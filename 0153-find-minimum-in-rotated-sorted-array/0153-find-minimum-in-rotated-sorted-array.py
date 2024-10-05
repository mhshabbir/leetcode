class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
                        R
                    M
                0,1,2,3,4
        nums = [3,4,5,1,2]
                      L
        
        if my m is less than R: 
            smallest value is in the left side
        
        if my m is bigger than R than means the smaller value is in right side
        """

        left, right = 0, len(nums) - 1
        res = float('inf')
        while left <= right:
            mid = left + (right - left)//2
            # print(left, mid, right)
            if nums[mid] <= nums[right]:
                right = mid - 1
                res = min(nums[mid], res)
            else:
                left = mid + 1
        return res