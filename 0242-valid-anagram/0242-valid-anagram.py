class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)

        for char in t:
            if char not in count or (count[char] - 1 == -1):
                return False
            else:
                count[char] -= 1
        return True