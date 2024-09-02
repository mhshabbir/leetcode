class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        """
        Always even length
        arr = []
        both alice and bob removes min i from nums
        both will get equal chances because its equal len(nums)
        both bob and alice append the arr with min i
        """

        """
        nums = [5,4,2,3]
        """
        arr = []
        heapq.heapify(nums)
        while len(nums) > 0:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            arr.append(bob)
            arr.append(alice)
        
        return arr