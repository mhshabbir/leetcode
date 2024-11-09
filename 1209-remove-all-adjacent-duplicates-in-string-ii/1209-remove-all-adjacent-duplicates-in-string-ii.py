class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for letter in s:
            if stack and stack[-1][0] == letter:
                letter, count = stack.pop()
                stack.append((letter, count + 1))
            else:
                stack.append((letter, 1))

            if stack[-1][1] == k:
                stack.pop()

        result = ""
        while stack:
            string, count = stack.pop()
            result = (string * count) + result

        return result
        
            
