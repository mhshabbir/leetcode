class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Approach 1: to assign a pointer in the front and a pointer in the back
        use a temp to swap the ptrs
        """

        l = 0
        r = len(s) - 1
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
         
        