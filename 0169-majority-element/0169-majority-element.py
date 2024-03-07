class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Solution 1:
        store all the elements in hashmap and count using iteration. 
        check if the count if more than n/2 after adding it to the hash
        """
        countHash = {}

        for i in nums:
            countHash[i] = 1 + countHash.get(i,0)
            if countHash[i] > len(nums)//2:
                return i
            