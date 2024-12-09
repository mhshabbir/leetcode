class Solution:
    def isPalindrome(self, x: int) -> bool:
        # arr = []
        # num = str(x)
        # if num[0] == "-": return False
        
        # for i in range(len(num)):
        #         arr.append(num[i])

        # return arr == arr[::-1]
        if x < 0: return False

        div = 1
        while x >= 10 * div:
            div *= 10
        while x:
            left = x // div
            right = x % 10

            if left != right: return False

            x = (x % div) // 10

            div = div / 100
        return True

        