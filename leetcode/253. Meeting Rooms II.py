from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        
        h = []
        max_overlap = 0
        
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            
            if len(h) == 0:
                heappush(h, end)
            else:
                while len(h) != 0 and start >= h[0]:
                    heappop(h)
                heappush(h, end)
            
            max_overlap = max(max_overlap, len(h))
        
        return max_overlap
            
        
