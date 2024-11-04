class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def getSum(cur):
            squaredSum = 0
            while cur != 0:
                squaredSum = math.pow((cur%10), 2)
                cur = cur//10

            return squaredSum

        while n not in visited:
            n = getSum(n)
            visited.add(n)
            if n == 1:
                return True
        
        return False
