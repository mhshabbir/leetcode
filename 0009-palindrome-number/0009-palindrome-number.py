class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = []
        num = str(x)
        if num[0] == "-":
            for i in range(1, len(num)):
                if num[0] == "-" and i == 1:
                    arr.append("-"+num[i])
                else:
                    arr.append(num[i])
        else:
            for i in range(len(num)):
                    arr.append(num[i])
        print(arr)
        left = 0
        right = len(arr) - 1
        if int(arr[0]) < 0 and len(arr) == 1:
            return False
        while left < right:
            if arr[left] == arr[right]:
                left += 1
                right -= 1
            else:
                return False
        return True