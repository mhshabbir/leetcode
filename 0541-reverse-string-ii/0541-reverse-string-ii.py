class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        strList = list(s)
        n = len(s)

        for i in range(0, n, 2 * k):
            strList[i:i+k] = reversed(strList[i:i+k])

        return "".join(strList)
