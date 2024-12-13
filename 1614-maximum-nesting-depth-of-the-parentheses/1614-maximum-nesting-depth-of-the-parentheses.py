class Solution:
    def maxDepth(self, s: str) -> int:
        """
        (1+(2*3)+((8)/4))+1
                 ^
        m = 2
        c = 1
        (  () ((
        []
        
        """
        max_param = 0
        count_open_param = 0
        for ptr in s:
            if ptr == "(":
                count_open_param += 1
                max_param = max(max_param, count_open_param)
            elif ptr == ")":
                count_open_param -= 1
            

        return max_param