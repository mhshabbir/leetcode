class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # sortedNums = 
        # nums.sort()
        # count = 1
        # output = 1
        # if len(nums) == 0:
        #     return 0
        # # print(len(nums))
        # # print(len(nums)-2)
        # for i in range(len(nums)-1):
        #     print(nums[i])
        #     if (nums[i] + 1) == nums[i+1]:
        #         print(nums[i],nums[i+1])
        #         count += 1
        #     else:
        #         if count > output:
        #             output = count
        #     if count > output:
        #         output = count
        # return output
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
