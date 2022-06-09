class UndergroundSystem:

    def __init__(self):
        def default_value():
            return (0, 0)

        self.dic = defaultdict(default_value) # (start, end) -> (total_time, count)
        self.id_to_ts = {} # id -> (station, checkin timestamp)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_to_ts[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_t = self.id_to_ts[id]
        total_time, count = self.dic[(start_station, stationName)]
        self.dic[(start_station, stationName)] = (total_time+t-start_t, count+1)
        del self.id_to_ts[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.dic[(startStation, endStation)]
        return total_time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
