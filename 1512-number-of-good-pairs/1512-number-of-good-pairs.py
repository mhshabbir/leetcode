class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
         
        
        """
        output = 0
        hashMap = Counter(nums)
        for key in hashMap.keys():
            n = hashMap[key]
            pairs = n*(n-1)//2
            output += pairs
        return output 
            