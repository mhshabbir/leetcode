class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = strs[0]
        for word in strs:
            indexI = 0
            indexJ = 0
            while indexI < len(word) and indexJ < len(longestPrefix):
                if longestPrefix[indexJ] == word[indexI]:
                    indexJ += 1
                    indexI += 1
                else:
                    break
            longestPrefix = longestPrefix[0:indexI]
        return longestPrefix