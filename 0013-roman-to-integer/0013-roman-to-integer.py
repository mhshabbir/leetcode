class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanMap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        for char in range(len(s)):
            if char + 1 < len(s):
                if s[char] == "I" and (s[char+1] == "V" or s[char+1] == "X"):
                    total += -(romanMap[s[char]])
                elif s[char] == "X" and (s[char+1] == "L" or s[char+1] == "C"):
                    total += -(romanMap[s[char]])
                elif s[char] == "C" and (s[char+1] == "D" or s[char+1] == "M"):
                    total += -(romanMap[s[char]])
                else:
                    total += (romanMap[s[char]])
        return total + romanMap[s[-1]]