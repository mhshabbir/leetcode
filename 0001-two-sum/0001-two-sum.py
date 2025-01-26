class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [2,7,11,15]
        if 9-2 in {} else add it
        {}

        """

        hashmap = {}
        for index, num in enumerate(nums):
            if (target - num) in hashmap:
                return [hashmap[target-num], index]
            else:
                hashmap[num] = index