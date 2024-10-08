class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        g = [1,2,3], s = [1,1]
               ^             V
        g = [10,9,8,7], s = [5,6,7,8]
             ^                
        
        """
        contentChildren = 0
        ptr1 = 0
        ptr2 = 0
        g.sort()
        s.sort()
        while ptr1 < len(g) and ptr2 < len(s):
            if s[ptr2] >= g[ptr1]:
                contentChildren += 1
                ptr1 += 1
                ptr2 += 1
            else: 
                ptr2 += 1
        
        return contentChildren