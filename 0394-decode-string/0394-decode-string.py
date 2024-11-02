class Solution:
    def decodeString(self, s: str) -> str:
        """
        [aaa]
        """
        stack = []
        for i in range(len(s)):
            print(i)
            if s[i] != "]":
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substring)
            print(stack)

        return "".join(stack)
