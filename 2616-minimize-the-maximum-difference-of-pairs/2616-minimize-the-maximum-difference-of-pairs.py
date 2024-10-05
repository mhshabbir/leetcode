class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """   
            # nums = [10,1,2,7,1,3]
                                    M      R
            # nums.sort() = [1, 1, 2, 3, 7, 10]
                            L
                            [-1, 0, 1, 1, 4, 3]
            # nums = [4,2,1,2]
            # nums.sort() = [1, 2, 2, 4]
        """
        def isValid(thresold):
            i, count = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= thresold:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    return True
            return False
        if p == 0: return 0
        nums.sort()
        left, right = 0, 10**9
        res = 10**9
        while left <= right:
            mid = left + (right - left)//2
            if isValid(mid):
                right = mid - 1
                res = mid
            else:
                left = mid + 1
            
        return res
