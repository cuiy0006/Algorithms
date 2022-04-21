"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = [interval for employee in schedule for interval in employee]
        
        intervals.sort(key=lambda interval:interval.start)
        
        max_end = intervals[0].end

        res = []
        for interval in intervals:
            if interval.start > max_end:
                res.append(Interval(max_end, interval.start))
            
            max_end = max(max_end, interval.end)
        
        return res
