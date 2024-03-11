class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        If the num in 
        
        """

        nums1Idx = {n:i for i,n in enumerate(nums1)} #  {4:0, 1:1, 2:2}
        res = [-1] * len(nums1)
        stack = []  # [2, 4]

        for i in range(len(nums2)):
            cur = nums2[i]  #cur = 2
            while stack and cur > stack[-1]: #stack[-1] = 4
                val = stack.pop() #val = 1
                idx = nums1Idx[val] #idx = 1
                res[idx] = cur # [-1,3,-1]
            if cur in nums1Idx:# [2]
                stack.append(cur)
        return res