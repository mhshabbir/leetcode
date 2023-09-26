class Solution:
    def isValid(self, s: str) -> bool:
        # """
        #     Brute Force: 
        # """
        # stack = []
        # roundB = 0
        # curlyB = 0  
        # squareB = 0
        # for bracket in s:
        #     if bracket == "(":
        #         roundB += 1
        #     elif bracket == ")":
        #         roundB -= 1
        #     elif bracket == "{":
        #         curlyB += 1
        #     elif bracket == "}":
        #         curlyB -= 1
        #     elif bracket == "[":
        #         squareB += 1
        #     elif bracket == "]":
        #         squareB -= 1

        # if roundB < 0 or curlyB < 0 or squareB < 0:
        #         return False
            
        # if roundB + curlyB + squareB == 0:
        #     return True
        # else:
        #     return False

        # stack = []
        # hashmap = {")":"(", "]":"[", "}":"{"}
        # for char in s:
        #     if char == "(" or char == "{" or char == "[":
        #         stack.append(char)
        #     elif char in hashmap:
        #         if stack and stack[-1] == hashmap[char]:
        #             stack.pop()
        #     else:
        #         return False

        # return True if stack else False

        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack 
            
                
















        
            