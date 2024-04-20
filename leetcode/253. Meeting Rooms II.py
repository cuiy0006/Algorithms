class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 0                30
        #    5 10 
        #           15 20
        res = 0
        intervals.sort(key=lambda x:x[0])
        h = []
        for [start, end] in intervals:
            while len(h) != 0 and h[0] <= start:
                heappop(h)
            heappush(h, end)
            res = max(res, len(h))
        return res

