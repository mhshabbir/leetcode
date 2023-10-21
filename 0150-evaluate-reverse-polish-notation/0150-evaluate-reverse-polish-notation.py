class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Because the order matters:
            stack, res
        ["2","1","+","3","*"]
        
        2,1,+
        2+1 = 3


        ["4","13","5","/","+"]
        4,13,5 /
        """

        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            else: 
                stack.append(int(c))
        return stack[0]