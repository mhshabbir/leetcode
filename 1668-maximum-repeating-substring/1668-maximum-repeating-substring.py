class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        i = 0
        max_rep = 0

        while i < len(sequence):
            rep = 0
            while sequence[i: i+len(word)] == word:
                rep += 1
                i = i + len(word)
            if rep:
                max_rep = max(rep, max_rep)
                i -= len(word)
            i += 1
        return max_rep

