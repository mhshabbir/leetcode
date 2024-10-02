class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        make a possiblity function if the arrays segments can fit the capcity or not:
        return true or false
        """

        # return t if the all the elements fits the arrays
        def possible(capcity):
            sum = 0
            number_of_days = 1
            for weight in weights:
                if (sum + weight) <= capcity:
                    sum += weight
                else:
                    sum = weight
                    number_of_days += 1
            if number_of_days > days:
                return False
            else:
                return True
        res = 0
        
        l = max(weights)
        r = sum(weights)
        while l<=r:
            m = (l+r)//2
            if possible(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res


