class Solution:
    def equalFrequency(self, word: str) -> bool:
        # letter_count = Counter(word)

        # max_freq = max(letter_count.values())
        # min_freq = min(letter_count.values())

        #     # 1 == 1 
        # if max_freq == min_freq == 1:
        #     return True
        # elif max_freq == min_freq or (max_freq - min_freq) > 1:
        #     return False
        # else:
        #     return True
        cnt = Counter(Counter(word).values())
        if (len(cnt) == 1):
            return list(cnt.keys())[0] == 1 or list(cnt.values())[0] == 1
        if (len(cnt) == 2):
            f1, f2 = min(cnt.keys()), max(cnt.keys())
            return (f1 + 1 == f2 and cnt[f2] == 1) or (f1 == 1 and cnt[f1] == 1)
        return False