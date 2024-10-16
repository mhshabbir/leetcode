class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        """
        [1,1,1,3,3,3,7]

        [0,1,2,3,4,5,6]
        0,1 1,2 0,1 

        """
        powersOfTwo = [2**i for i in range(22)]
        
        # print(powersOfTwo)
        # powersOfTwo = {1,2,4,8,16}
        # mealCount = Counter(deliciousness)
        # {1:3, 3:3, 7:1}

        mp = {}
        ans = 0
        for x in deliciousness:
            for i in powersOfTwo:
                if (i - x) in mp:
                    print(i-x, mp, ans)
                    ans += mp[i - x]
            mp[x] = mp.get(x, 0) + 1
            print(mp)

        return ans % (10**9 + 7)
        

                    