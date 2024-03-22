class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = 1
        intervals.sort(key=lambda x:(x[0], -x[1]))
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= curr[1]:
                continue
            res += 1
            curr = intervals[i]
        
        return res