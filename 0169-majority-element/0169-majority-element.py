class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Solution 1:
        store all the elements in hashmap and count using iteration. 
        check if the count if more than n/2 after adding it to the hash
        """
        # countHash = {}

        # for i in nums:
        #     countHash[i] = 1 + countHash.get(i,0)
        #     if countHash[i] > len(nums)//2:
        #         return i

        """
        BOYER MOORE Algorithm
        Because the majority element always appears more than half the elements in the array, count the number 
        of element and deduct the non majority element from it
        """
        count = 0
        res = 0
        for n in nums:
            if count == 0:
                res = n
            
            count += (1 if n == res else -1)
        return res


            