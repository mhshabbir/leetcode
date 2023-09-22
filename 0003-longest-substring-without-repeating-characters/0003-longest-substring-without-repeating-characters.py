class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # """
        #    vR
        # "abcabcbb"
        #  ^L
        # """
        # if len(s) == 0:
        #     return 0
        # elif len(s) == 1:
        #     return 1
        # left = 0
        # right = left + 1
        # output = 0
        # counter = 1  #2
        # while right < len(s):
        #     if s[left] == s[right]: # false condition 
        #         left = right
        #         right = right + 1
        #     else:
        #         counter += 1
        #         right += 1
        #     output = max(counter, output)
        # return output

        # if len(s) == 0:
        #     return 0
        # elif len(s) == 1:
        #     return 1
        # left = 0
        # right = 0
        # output = 0
        # counter = 1 #2
        # visited = set()
        # while right < len(s):
        #     if s[right] in visited:
        #         while s[right] in visited:
        #             visited.remove(s[left])
        #             left =+ 1
        #         visited.add(s[right])
        #     else:
        #         visited.add(s[right])
        #         right += 1
        #         counter = right - left
        #     output = max(counter,output)

        # return output 
        visited = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            res = max(res, right - left + 1)
        return res
            
