class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        dupSet = set()
        for R in range(len(nums)):
            if R-L > k:
                dupSet.remove(nums[L])
                L += 1
            if nums[R] in dupSet:
                return True
            dupSet.add(nums[R])
            
        return False