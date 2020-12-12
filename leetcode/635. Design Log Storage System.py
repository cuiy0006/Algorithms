class LogSystem:

    def __init__(self):
        self.dic = {'Year':1, 'Month':2, 'Day':3, 'Hour':4, 'Minute':5, 'Second':6}
        self.lst = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        time = [int(item) for item in timestamp.split(':')]
        time = tuple(time)
        self.lst.append((time, id))
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        start = [int(item) for item in s.split(':')]
        start = tuple(start)
        end = [int(item) for item in e.split(':')]
        end = tuple(end)
        idx = self.dic[gra]
        res = []
        for time, id in self.lst:
            if time[:idx] >= start[:idx] and time[:idx] <= end[:idx]:
                res.append(id)
        return res
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
