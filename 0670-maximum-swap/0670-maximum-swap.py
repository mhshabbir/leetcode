class Solution:
    def maximumSwap(self, num: int) -> int:
        numList = list(str(num))
        
        maxDigit = "0"
        max_i = -1
        swap_i = swap_j = -1

        for i in reversed(range(len(numList))):
            if numList[i] > maxDigit:
                maxDigit = numList[i]
                max_i = i
            if numList[i] < maxDigit:
                swap_i = i
                swap_j = max_i
        numList[swap_i], numList[swap_j] = numList[swap_j], numList[swap_i]

        return int("".join(numList))
