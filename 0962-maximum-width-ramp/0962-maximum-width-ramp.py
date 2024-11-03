class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # p1
        # [9,10,1,0,1,9,4,0,4,1]
        #                    p2
        # diff = 5
        # indexDifference = +
        #  i
        # [0,1,2,3,4,5]
        #            j

        # i < j
        # if >= than move the j

        # nums[i] <= nums[j]
        maxArr = [0] * len(nums)
        maxInputNum = float('-inf')
        i = len(nums) - 1
        for maxNum in reversed(nums):
            maxInputNum = max(maxInputNum, maxNum)
            maxArr[i] = maxInputNum
            i -= 1
        
        result = 0
        left = 0
        #    l
        # [6,0,8,2,1,5]

        # [8,8,8,5,5,5]

        for right in range(len(nums)):
            while nums[left] > maxArr[right]:
                left += 1
            result = max(right - left, result)
        
        return result



            
