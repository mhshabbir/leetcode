class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        #      V
        # "aababcaab"
        #  ^
        # (a,b)
        # count = 2

        occ, n = collections.defaultdict(int), len(s)
        for i in range(n - minSize + 1):
            print(n - minSize + 1)
            print(s[i:i + minSize])
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                occ[sub] += 1
            
        return max(occ.values(), default=0)
