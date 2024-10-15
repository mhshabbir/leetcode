class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        print(allowedSet)
        res = 0
        for word in words:
            consistant = True
            for char in word:
                if char not in allowedSet:
                   consistant = False
            if consistant:
                res += 1
        return res