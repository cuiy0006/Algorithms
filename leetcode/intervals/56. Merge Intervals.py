class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        [start, end] = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                res.append([start, end])
                [start, end] = intervals[i]
            else:
                end = max(end, intervals[i][1])
        res.append([start, end])
        return res
