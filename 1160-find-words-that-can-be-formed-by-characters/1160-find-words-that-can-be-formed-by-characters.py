class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        """
        words = ["cat","bt","hat","tree"]
                    cat = [c,a,t]
                            c:1, a:1, t:1
        chars = atach
                    ^

                    {a:2, t:1, c:1, h:1}
        """

        charsCounter = Counter(chars)
        res = 0
        for word in words:
            wordCounter = Counter(word)

            #  c:1, a:1, t:1
            goodWord = True
            for char, num in wordCounter.items():
                if char not in charsCounter and num > charsCounter[char]:
                    goodWord = False
                    break
            if goodWord:
                res += len(word)
        return res
                
                                