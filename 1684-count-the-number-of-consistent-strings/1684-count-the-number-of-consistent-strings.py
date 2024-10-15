class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        print(allowedSet)
        res = 0
        for word in words:
            wordSet = set(word)
            if len(wordSet - allowedSet) == 0:
                res += 1
        return res