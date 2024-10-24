class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
            V
        [40,10,20,30]
          ^
        [10,20,30,40]
          ^
        """
        nums = sorted(arr)
        indexMap = {}

        rank = 1
        for r in range(len(nums)):
            if r > 0 and nums[r] == nums[r-1]:
                indexMap[nums[r]] = indexMap[nums[r-1]]
            else:
                indexMap[nums[r]] = rank
                rank += 1
        for i, num in enumerate(arr):
            arr[i] = indexMap[num]
        
        return arr
