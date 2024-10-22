class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            make the first element the longest prefix and use the rest of the element reducing the longest prefix.
        """
        longestPrefix = strs[0]
        for i in strs:
            indexI = 0
            indexJ = 0
            while indexI < len(i) and indexJ < len(longestPrefix):
                if longestPrefix[indexJ] == i[indexI]:
                    indexJ += 1
                    indexI += 1
                else:
                    break
            longestPrefix = longestPrefix[0:indexI]
        return longestPrefix