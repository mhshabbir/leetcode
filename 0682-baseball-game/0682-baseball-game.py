class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            print(i, res)
            if i == "C" and len(res):
                res.pop()
            elif i == "D" and len(res):
                res.append(res[-1]*2)
            elif i == "+" and len(res):
                res.append(res[-1] + res[-2])
            else:
                res.append(int(i))
            
        return sum(res)
