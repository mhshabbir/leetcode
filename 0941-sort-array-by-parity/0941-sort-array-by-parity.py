class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = []
        r = []
        for i in nums:
            if i%2 == 0:
                l.append(i)
            elif i%2 != 0:
                r.append(i) 
                
        return l+r