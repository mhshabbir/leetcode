class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # have = 0
        # need = len(t) #3

        # left, right = 0,0
        
        # win = {}
        # T = {}
        # res = ""
        # lenRes = 0

        # for character in t:  # {'A': 1, 'B': 1, 'C': 1} {'A': 0, 'B': 0, 'C': 0}
        #     T[character] = 1 + T.get(character, 0)
        #     win[character] = 0

        # while right < len(s) and left < len(s):
        #     if s[right] not in T:
        #         right += 1
        #     elif win[s[right]] == T[s[right]]:
        #         have += 1
        #         right += 1
        #     elif win[s[right]] > T[s[right]]:
        #         right += 1
        #     elif win[s[right]] < T[s[right]]:
        #         win[s[right]] += 1
        #         have += 1
                
            
        #     print("test")
            
        #     while have == need:
        #         if (right - left + 1) > lenRes:
        #             res = s[left:right + 1]
        #             lenRes = len(res)
                
        #         if s[left] in win:
        #             win[s[left]] -= 1
        #         if s[left] in T and win[s[left]] < T[s[left]]:
        #             have -= 1
        #         left += 1
        # return res

        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


            



        