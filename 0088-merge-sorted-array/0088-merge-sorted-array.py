class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = len(nums1) - 1
        n -= 1
        m -= 1
        while n > -1 and m > -1:
            if nums2[n] > nums1[m]:
                nums1[cur] = nums2[n]
                n -= 1
                cur -= 1
            else:
                nums1[cur] = nums1[m]
                m -= 1
                cur -= 1

        while n > -1:
            nums1[cur] = nums2[n]
            n -= 1
            cur -= 1
            
