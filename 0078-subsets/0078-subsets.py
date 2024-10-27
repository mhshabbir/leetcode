class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
               
           [0, 1]
            ^
           [], [0] [0,1] , [1]
        """
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # decision to add it
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to add it
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

