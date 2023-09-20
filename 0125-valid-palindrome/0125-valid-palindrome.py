class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Remove all the non letters. 
        Place 2 pointers, one in the front and one in the back. 
        loop through them to match the letters until 2 pointers meet. 
        """
          
        l = 0
        r = len(s)-1
        #print(r)
        
        while l <= r:
            if s[l].isalnum():
                #print(s[l])
                if s[r].isalnum():
                    #print(s[r])
                    if(s[r].lower() != s[l].lower()):
                        return False
                    else:
                        l += 1
                        r -= 1
                else:
                    r -= 1
            else:
                l += 1
        return True

        # point1 = 0
        # point2 = len(s) - 1
        # while point1 < point2 :
        #     if ord(s[point1].lower()) < ord("a") and ord(s[point1].lower()) > ord("z"):
        #         point1 += 1
        #         continue
        #     if ord(s[point2].lower()) < ord("a") and ord(s[point2].lower()) > ord("z"):
        #         point2 -= 1
        #         continue
        #     if s[point1].lower() != s[point2].lower():
        #         return False
        # return True
                
            













