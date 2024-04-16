class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # numsHash = set(nums)
        # res = []
        # for i in range(1,len(nums)+1):
        #     if i not in numsHash:
        #         res.append(i)
        
        # return res
        res = []
        for i, n in enumerate(nums):
            # print(i,n,nums)
            nums[abs(n)- 1] = abs(nums[abs(n) - 1]) * -1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res