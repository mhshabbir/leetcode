class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # """
        #     U:
        #     return the indices of elements which adds up to T

        #     M:
        #     using Hashmap to record the element
        #     2 For loops

        #     P:
        #     hashmap = { element : index }
        #     Target = 9
        #     [2,7,11,15]
        #      check if the compliment exist
            
        #      ^ 
        #      { 2 : 0 , }
        #     saving the compliment to the hashmaps

        #     I: 
        #     R:
        # """
        targetMap = {}
        #  0 , 2
        for i,n in enumerate(nums):
            # 9 - 7 = 2
            if (target - n) in targetMap:
                index = targetMap[(target - n)]
                return [index, i]
            else:
                targetMap[n] = i

            