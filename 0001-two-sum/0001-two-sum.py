class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for index,num in enumerate(nums):
            # 9 - 2 = 7
            if (target - num) in hashset:
                return [index, hashset[(target - num)]]
            else:
                hashset[num] = index
        