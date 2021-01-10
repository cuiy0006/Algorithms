class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        i = 0
        j = 1
        cnt = 0
        while j < len(intervals):
            if intervals[i][1] <= intervals[j][0]:
                i = j
            else:
                cnt += 1
            j += 1
        return cnt
        
