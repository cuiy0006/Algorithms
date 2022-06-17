class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(n+1):
            start = max(0, i-ranges[i])
            end = min(n, i+ranges[i])
            intervals.append((start, end))
        
        intervals.sort(key=lambda x:(x[0], -x[1]))
        dp = [sys.maxsize for _ in range(n+1)]
        
        for i, (start, end) in enumerate(intervals):
            if i > 0 and start == intervals[i-1]:
                continue
            if i == 0:
                base = 0
            else:
                base = dp[start]
            
            if i != 0 and base == sys.maxsize:
                return -1
            
            for j in range(start, end+1):
                dp[j] = min(dp[j], base+1)

        if dp[n] == sys.maxsize:
            return -1
        else:
            return dp[n]
