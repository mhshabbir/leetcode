class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashset = {}
        for n,i in enumerate(nums):
            if (target - i) in hashset:
                return [hashset[target-i], n]
            else:
                hashset[i] = n
        
