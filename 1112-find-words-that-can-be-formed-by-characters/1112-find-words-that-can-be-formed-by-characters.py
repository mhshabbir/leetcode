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

        count = Counter(chars)
        res = 0
        for word in words:
            cur = defaultdict(int)
            #  c:1, a:1, t:1
            goodWord = True
            for char in word:
                cur[char] += 1
                if char not in count or cur[char] > count[char]:
                    goodWord = False
                    break
            if goodWord:
                res += len(word)
        return res
                
                                