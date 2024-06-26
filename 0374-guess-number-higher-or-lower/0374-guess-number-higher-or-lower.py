# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        top = n
        bottom = 1
        while True:
            myGuess = random.randint(bottom, top)
            guessNum = guess(myGuess)
            if guessNum == 0:
                return myGuess
            elif guessNum == -1: #means that its higher
                top = myGuess - 1
            else:
                bottom = myGuess + 1