class UndergroundSystem:

    def __init__(self):
        self.d={}
        self.ans={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,time=self.d[id]
        if (start,stationName) not in self.ans:
            self.ans[(start,stationName)]=[0,0]
        self.ans[(start,stationName)][0]+=t-time
        self.ans[(start,stationName)][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t,c=self.ans[(startStation,endStation)]
        return t/c


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)