class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1ptr = 0
        word2ptr = 0
        res = ""

        while word1ptr < len(word1) and word2ptr < len(word2):
            res += word1[word1ptr]
            word1ptr += 1
            res += word2[word2ptr]
            word2ptr += 1

        print(word1ptr, len(word1) - 1, word2ptr,len(word2) - 1)
        if word1ptr != len(word1):
            res = res + word1[word1ptr:len(word1)]
            
        if word2ptr != len(word2):
            res = res + word2[word2ptr:len(word2)]

        return res
            
