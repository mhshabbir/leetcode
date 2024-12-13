class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Step 1: Put all the nums in hashmap 
        Step 2: Iterate through all of them and the count of each
        Add them to res
        """

        # res = []
        # hashmap = {}

        # for num in nums:
        #     hashmap[num] = 1 + hashmap.get(num,0)
        # print(hashmap)

        # for num in hashmap.keys():
        #     if hashmap[num] >= k:
        #         res.append(num)
        # return res

        count = Counter(nums)
        top_k = list(count.values())
        
        result = []
        heapq.heapify(top_k)
        for i in range(k):
            result.append(heapq.heappop(top_k))
        return result

