class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
              V
        "abcabcbb"
                  ^
        max = 3

        """
        max_length = 0
        left = 0
        right = 0
        unique = set()
        while right < len(s):
            if s[right] in unique:
                unique.remove(s[left])
                left += 1
            else:
                unique.add(s[right])
                max_length = max(len(unique), max_length)
                right += 1
        
        return max_length