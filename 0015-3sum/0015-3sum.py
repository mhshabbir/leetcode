class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visitedElement = set()
        output = []
        for i,num in enumerate(nums):
            if num in visitedElement:
                continue
            else:
                visitedElement.add(num)
            diff = 0 - num # 0 - (-4) = 4
            left = i+1
            right = len(nums) - 1 
            while right > left:
                sum = nums[left] + nums [right]
                if sum > diff:
                    right -= 1
                elif sum < diff:
                    left += 1
                else:
                    output.append([num,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
        return output

