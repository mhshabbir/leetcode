class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # count = 0
        # for left in range(len(s)):
        #     right = left + 1
        #     swaps = k
        #     while right < len(s):
        #         if s[right] != s[left]:
        #             if swaps == 0:
        #                 count = max(count, right - left)
        #                 break
        #             else:
        #                 swaps -= 1
        #                 right += 1
        #         else:
        #             right += 1
        #         count = max(count, right - left)
        # return count
        # charDict = {}
        # left, right = 0, 0
        # maxChar = 0
        # output = 0
        # while right < len(s):
        #     if (right - left) - maxChar <= k:
        #         charDict[s[right]] = 1 + charDict.get(right, 0)
        #         maxChar = max(maxChar, charDict[s[right]])
        #         output = max((right - left),output)
        #     else:
        #         charDict[s[left]] = charDict.get(left, 0) - 1
        #         maxChar = max(charDict.values())
        #         left += 1
        #         output = max((right - left),output)
        #     right += 1    
                
        
        # return output
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
            
