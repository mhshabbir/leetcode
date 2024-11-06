class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = []
        maxright = []

        maxheight_l = 0
        maxheight_r = 0

        for i in range(len(height)):
            maxheight_l = max(height[i], maxheight_l)
            maxleft.append(maxheight_l)

        print(maxleft)

        for i in reversed(height):
            maxheight_r = max(i, maxheight_r)
            maxright.append(maxheight_r)

        maxright = maxright[::-1]
        minDiff = []
        # print(maxleft)
        print(maxright)

        for l, r in zip(maxleft,maxright):
            minDiff.append(min(l, r))
        
        print(minDiff)
        result = 0
        for i in range(len(height)):
            waterCollected = minDiff[i] - height[i]
            if waterCollected > 0:
                result += waterCollected
        
        return result
