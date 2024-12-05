class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.keyArr = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        else:
            self.keyArr.append(val)
            self.hashmap[val] = len(self.keyArr) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            # find the index for the array
            arrayKey = self.hashmap[val]
            # replace the index with the last element of the array
            self.keyArr[arrayKey] = self.keyArr[-1]
            # update the keyindex with the hashmap
            self.hashmap[self.keyArr[arrayKey]] = arrayKey
            # delete the last index
            self.keyArr.pop()
            # delete the hashmap for the value
            del self.hashmap[val]
            return True
        return False

    def getRandom(self) -> int:
        return self.keyArr[random.randint(0, len(self.keyArr)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()