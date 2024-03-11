class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        ptr1, last = m - 1,  len(nums1) - 1
        ptr3 = len(nums2) - 1

        while ptr1 > -1 and ptr3 > -1:
            print(nums1, ptr1, ptr3, last)
            if nums2[ptr3] > nums1[ptr1]:
                nums1[last] = nums2[ptr3]
                ptr3 -= 1
            else:
                nums1[last] = nums1[ptr1]
                ptr1 -= 1
            last -= 1
        print("after",nums1, ptr1, ptr3, last)
        while ptr3 > -1:
            print("after",nums1, ptr1, ptr3, last)
            nums1[last] = nums2[ptr3]
            ptr3 -= 1
            last -= 1
    