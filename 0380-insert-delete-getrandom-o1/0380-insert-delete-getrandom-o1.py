class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.valArray = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.valArray)
        self.valArray.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        index = self.dict[val]
        temp = self.valArray[-1]
        self.valArray[-1] = self.valArray[index]
        self.valArray[index] = temp
        self.dict[temp] = index
        del self.dict[val]
        return self.valArray.pop(len(self.valArray)-1)

    def getRandom(self) -> int:
        return random.choice(self.valArray)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()