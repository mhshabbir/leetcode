class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """         
            a = "1010", 
            a = "0101"
                    ^
            b = "1101"
                    ^
                 1010

            carry = 1
        """
        n = max(len(a), len(b))
        a, b = a[::-1], b[::-1]
        carry = 0
        res = ""         
        print("digitA, digitB, total, carry, total%2, total//2")
        for i in range(n):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            # print(digitA, digitB, total, carry, total%2, total//2)
            res = str(total%2) + res
            carry = total // 2
            # print(carry)

        if carry:
            res = str(carry) + res

        return res