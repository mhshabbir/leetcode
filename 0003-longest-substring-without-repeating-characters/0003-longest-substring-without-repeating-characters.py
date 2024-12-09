class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #      V
        # pwwkew
        #      ^   

        longest_substr = 0
        l = 0
        substr_set = set()
        for r in range(len(s)):
            if s[r] in substr_set:
                while s[r] in substr_set:
                    substr_set.remove(s[l])
                    l += 1
            substr_set.add(s[r])
                
            longest_substr = max(longest_substr, len(substr_set))
        
        return longest_substr
