class MyCalendarTwo:

    def __init__(self):
        self.intervals = []
        self.double = []

    def book(self, startTime: int, endTime: int) -> bool:
        def overlap(start1, end1, start2, end2):
            return (start1 <= start2 and end1 > start2) or (start1 >= start2 and start1 < end2)

        for start, end in self.double:
            if overlap(start, end, startTime, endTime):
                return False
        
        for start, end in self.intervals:
            if overlap(start, end, startTime, endTime):
                self.double.append((max(start, startTime), min(end, endTime)))

        self.intervals.append((startTime, endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
