class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], interval[1]))
        i = 0
        j = 1
        cnt = 0
        while j < len(intervals):
            if intervals[i][1] <= intervals[j][0]:
                i = j
            elif intervals[i][1] > intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                cnt += 1
            else:
                i = j
                cnt += 1
            j += 1
        return cnt
        
