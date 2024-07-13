class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        red = 0, white = 1, and blue = 2
        nums =   [2,0,2,1,1,0]
        output = [0,0,1,1,2,2]
        Input: nums = [2,0,1]
        Output: [0,1,2]


        U         
        Time: O(N)
        Space: Open

                        V  
        nums =   [0,0,1,2,1,2]
                      ^
                        R
        nums =   [0,0,1,1,2,2]
                        l
                       r
        Example = [1,0,2]
                   l
                   
        While R > l:
            L > R:
                R-1
                L+1
            If switch is not made:
                L+1
        return Array
                            V3
                            r               
        nums =   [0,0,1,1,2,2]
                          l

                        r  
                      V                                   
        nums =   [0,0,1,1,2,2]
                      l
                  r
                    V
        nums = [0,1,2]
                  l
        While r > l:         
        if s[V] == 0:
            temp = s[l]
            s[l] = s[v]
            s[V] = temp
            l += 1
            V += 1
        elif s[V] == 2:
            temp = s[r]
            s[r] = s[v]
            s[V] = temp
            r -=1
        else:
            V += 1
        ans: [0,0,1,2,1,2]
                 r
             V
        [0,0,2,1,1,2]
             l
        M
        P
        I
        R
        E
        """
        l = 0
        v = 0
        r = len(nums) - 1

        while r > l and v <= r:
            print(nums[l], nums[v], nums[r], nums)
            if nums[v] == 0:
                temp = nums[l]
                nums[l] = nums[v]
                nums[v] = temp
                l += 1
                v += 1
                print("if",nums)
            elif nums[v] == 2:
                temp = nums[r]
                nums[r] = nums[v]
                nums[v] = temp
                r -=1
                print("else",nums)
            else:
                v += 1
                print("else3",nums)
            
            print(nums[l], nums[v], nums[r], nums)


        