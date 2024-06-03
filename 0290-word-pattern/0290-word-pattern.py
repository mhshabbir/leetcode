class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Note: pattern and s are in str

        get the pattern into numbers:
        a = 0
        b = 1
        c = 2

        get the s in numbers as well
        0 = dog
        1 = cat
        2 = fist

        have 1 for loop and 2 hashmaps

        """
        hashPattern = {}
        #{"a" : "dog", "b": "cat"}
        patternWord = s.split()
        #[dog, cat, cat, dog]
        for i in range(len(pattern)):
            hashPattern[pattern[i]] = patternWord[i]

        returnS = []
        for i in range(len(pattern)):
            print(i)
            returnS.append(hashPattern[pattern[i]])
        
        return True if patternWord == returnS else False


