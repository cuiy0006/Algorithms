class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        intervals.sort(key=lambda x:x[0])
        
        curr = intervals[0]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] > curr[1]:
                res.append(curr)
                curr = interval
            else:
                curr[1] = max(curr[1], interval[1])
        
        res.append(curr)
        return res
