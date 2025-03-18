class Solution:
    def compress(self, chars: List[str]) -> int:

        """
        ["a","a","b","b","c","c","c"]
                                     ^

         stack [a, 2, b, 2, c, 3] 
        """
        stack = []
        i = 0
        while i < len(chars):
            count = 1
            stack.append(chars[i])

            while (i + 1) < len(chars) and chars[i + 1] == stack[-1]:
                count += 1
                i += 1
            
            if count > 1:
                stack.extend(list(str(count)))
            
            i += 1
        
        for i in range(len(stack)):
            chars[i] = stack[i]
        
        return len("".join(stack))

