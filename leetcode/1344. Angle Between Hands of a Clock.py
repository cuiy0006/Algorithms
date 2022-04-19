class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_percent = minutes / 60
        hour_percent = hour % 12 / 12
        
        minute_degree = 360 * minute_percent
        
        hour_degree = hour_percent * 360 + minute_percent * 360 / 12
        
        diff = abs(hour_degree - minute_degree)
        if diff <= 180:
            return diff
        else:
            return 360 - diff
