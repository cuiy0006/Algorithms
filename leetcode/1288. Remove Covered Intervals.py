class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        
        res = 1
        curr = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[1] <= curr[1]:
                continue
            else:
                curr = interval
                res += 1
        
        return res
