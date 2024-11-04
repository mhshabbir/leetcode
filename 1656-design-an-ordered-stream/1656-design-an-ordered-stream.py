class OrderedStream:

    def __init__(self, n: int):
        self.orderArr = [""] * n
        self.ptr = 0

    #  0   1   2   3   4 
    # [a, b, c, "", ""]

    def insert(self, idKey: int, value: str) -> List[str]:
        self.orderArr[idKey-1] = value
        if self.orderArr[self.ptr] != "":
            while self.ptr < len(self.orderArr) and self.orderArr[self.ptr] != "":
                self.ptr += 1
            return self.orderArr[idKey - 1:self.ptr]
        else:
            return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)