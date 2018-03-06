# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        res = []
        for i, interval in enumerate(intervals):
            if interval.end < start or interval.start > end:
                res.append(interval)
            else:
                start = min(start, interval.start)
                end = max(end, interval.end)
        j = 0
        while j < len(res):
            if start > res[j].start:
                j += 1
            else:
                break
        res.insert(j, Interval(start, end))
        return res
