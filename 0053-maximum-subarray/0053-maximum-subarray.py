class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-2,1,-3,4,-1,2,1,-5,4]
        #  [4,-1, 2, 1,-5,4   ] 

        total = 0
        maxSubArrSum = float('-inf')
        for num in nums:
            total += num
            if total < 0:
                total = 0
            maxSubArrSum = max(total, maxSubArrSum)

        return maxSubArrSum
