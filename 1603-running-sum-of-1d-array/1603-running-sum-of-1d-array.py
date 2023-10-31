class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        prev = 0
        for num in nums:
            prev += num
            res.append(prev)
        return res
            
