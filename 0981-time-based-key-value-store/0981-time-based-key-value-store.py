import collections
class TimeMap:

    def __init__(self):
        self.hashSet = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashSet[key].append((timestamp, value))    
        # print(self.hashSet)
    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashSet:
            searchArr = self.hashSet[key]

            left, right = 0, len(searchArr) - 1
            res = ""
            while left<=right:
                mid = left + (right - left)//2
                if searchArr[mid][0] < timestamp:
                    left = mid + 1
                    res = searchArr[mid][1]
                elif searchArr[mid][0] > timestamp:
                    right = mid - 1
                else:
                    return searchArr[mid][1]
            return res
        else:
            return ""
"""
    {"foo: [(1,"bar"), (2,"bar2")]"}

     
     m r
    [1,4]
     l
"""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)