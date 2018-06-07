# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x:x.start)
        res= []
        curr = None
        for interval in intervals:
            if curr == None:
                curr = interval
                continue
            if interval.start <= curr.end:
                curr.end = max(curr.end, interval.end)
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res
