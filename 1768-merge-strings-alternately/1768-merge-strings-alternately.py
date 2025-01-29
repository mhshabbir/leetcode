class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        
        for index in range(max(len(word1),len(word2))):
            if index < len(word1):
                char1 = word1[index]
            else:
                char1 = ""
            
            if index < len(word2):
                char2 = word2[index]
            else:
                char2 = ""
            
            res += char1 + char2
        return res