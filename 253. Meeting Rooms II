# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        curr = []
        intervals.sort(key = lambda x:(x.start, x.end))
        for interval in intervals:
            start = interval.start
            end = interval.end
            if len(curr) == 0:
                heappush(curr, end)
            else:
                if start >= curr[0]:
                    heappop(curr)
                heappush(curr, end)
        return len(curr)
