class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strInt = ""

        for num in digits:
            strInt += str(num)
        
        increment = int(strInt) + 1
        
        result = []

        while increment != 0:
            result.append(increment%10)
            increment = increment//10

        return result[::-1]
