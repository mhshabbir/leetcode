class Solution:
    def rob(self, nums: List[int]) -> int:
        # max_money = 0

        first_run = 0
        for i in range(0, len(nums), 2):
            first_run += nums[i]
        second_run = 0
        for i in range(1, len(nums), 2):
            second_run += nums[i]
        
        return max(first_run, second_run)