class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ptr1 = 0
        ptr2 = 0
        res = 0
        curSum = nums[0]

        """
        curSum = 5
              1V
        [1, 2, 3]
            2^
        
        """
        while ptr1 < len(nums) and ptr2 < len(nums):
            if curSum == k:
                res += 1
                while curSum == k and ptr1 >= ptr2:
                    curSum -= nums[ptr2]
                    ptr2 += 1
            elif ptr1 < len(nums) - 1:
                ptr1 += 1
                curSum += nums[ptr1]
            else:
                while ptr2 < len(nums):
                    if curSum == k:
                        res += 1
                        
                    curSum -= nums[ptr2]
                    ptr2 += 1
                    
            
        return res




            
            # curSum += nums[ptr1]
            # curSum 