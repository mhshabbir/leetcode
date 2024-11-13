class Solution:
    def addDigits(self, num: int) -> int:
        while num > 10:
            digitSum = 0
            while num != 0:
                digitSum
                digitSum += num%10
                num = num//10
            num = digitSum
        return num