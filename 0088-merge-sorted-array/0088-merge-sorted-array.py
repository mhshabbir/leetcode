class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """                V
        nums1 = [1,2,2,3,5,6]
                   ^   
                   m
        nums2 = [2,5,6]
                   ^
                   n
        """
        cur = len(nums1) - 1
        m = m - 1
        n = n - 1

        while n >= 0 and m >= 0:
            if nums1[m] >= nums2[n]:
                nums1[cur] = nums1[m]
                m = m - 1
            else:
                nums1[cur] = nums2[n]
                n = n - 1
            cur = cur - 1
        
        while n > -1:
            nums1[cur] = nums2[n]
            n = n - 1
            cur = cur - 1
            