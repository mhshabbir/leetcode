class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        max_count = 0

        for num in nums:
            if num - 1 not in nums_set:
                seq = num
                count = 0
                while seq in nums_set:
                    count += 1
                    seq += 1

                max_count = max(count, max_count)
        return max_count