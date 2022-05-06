from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        
        h = []
        for [start, end] in intervals:
            if len(h) == 0:
                heappush(h, end)
            else:
                if start >= h[0]:
                    heappop(h)
                heappush(h, end)
        
        return len(h)
