class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        r = sorted(nums)

        for start in range(N):
            # print(nums[start:] + nums[:start])
            # print(nums[start:])
            # print(nums[:start])
            if nums[start:] + nums[:start] == r:
                return True
        
        return False

