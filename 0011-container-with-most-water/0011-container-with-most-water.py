class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        
        # for i, elem in enumerate(height):
        #     left = 0
        #     right = left + 1
        #     area = 0
        #     print((len(height) -1))
        #     while right <= (len(height) -1):
        #         print(right)
        #         minElem = min(height[left],height[right])
        #         width = right - left
        #         if (minElem * width) > area:
        #             area = minElem * width
        #             right += 1
        #         else:
        #             right += 1
        #     max(area,maxArea)
        # return maxArea 
        left = 0
        right = len(height) -1
        while left != right:
            curArea = (min(height[left], height[right])) * (right - left)
            maxArea = max(maxArea, curArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
            
    