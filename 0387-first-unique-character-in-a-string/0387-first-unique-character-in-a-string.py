class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = Counter(s)

        for i, char in enumerate(s):
            if unique[char] == 1:
                return i
        return -1
            