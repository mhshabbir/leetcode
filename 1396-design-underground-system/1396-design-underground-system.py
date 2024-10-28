class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} # id -> (startion, time)
        self.totalMap = {} # (start, endstation) -> [totaltime, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        totaltime = t - self.checkInMap[id][1]
        start = self.checkInMap[id][0]
        if (start, stationName) not in self.totalMap:
            self.totalMap[(start, stationName)] = [0,0]
        self.totalMap[(start, stationName)][0] += totaltime
        self.totalMap[(start, stationName)][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.totalMap[(startStation, endStation)]

        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)