class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        
        for point in timePoints:
            hour, minute = point.split(':')
            minutes.append(60 * int(hour) + int(minute))
        
        minutes.sort()
        min_diff = 24 * 60
        
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
        min_diff = min(min_diff, 24 * 60 + minutes[0] - minutes[-1])
        
        return min_diff
